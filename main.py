import os
import sys 
from google import genai 
from google.genai import types
from dotenv import load_dotenv
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.get_file_content import schema_get_file_content, get_file_content 
from functions.write_file import schema_write_file, write_file 


system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents 
- Execute Python files with optional arguments
- Write or overwrite files 

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

availabe_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_run_python_file,
        schema_get_file_content,
        schema_write_file,
    ]
)

MAX_ITERS = 20

    
def main():
    # check if there is a prompt message (string) in cli call 
    if len(sys.argv) < 2:
        print("Usage: main.py 'your_prompt here'")
        sys.exit(1)

    verbose = "--verbose" in sys.argv 

    print("Sys argvs: ", sys.argv)
    user_prompt = sys.argv[1]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(
        role="user", 
        parts=[types.Part(text=user_prompt)]
        ),
    ]
    
    iters = 0 
    while True: 
        iters += 1
        if iters > MAX_ITERS:
            print(f"Maximum iterations reached. exiting...")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                    print("Final response: ")
                    print(final_response)
                    break
        except Exception as e:
            print(f"Error in generate content: {e}")

    
# generate the response, give the instructions and specify the model 
def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages, 
        config=types.GenerateContentConfig(system_instruction=system_prompt, tools=[availabe_functions]
        ),
    )

    if verbose: 
        print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
        print("Response tokens: ", response.usage_metadata.candidates_token_count)

    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content 
            messages.append(function_call_content)

    if not response.function_calls:
        return response.text 

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)

        if (not function_call_result.parts or not function_call_result.parts[0].function_response):
            raise Exception("empty function call result")

        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
            function_responses.append(function_call_result.parts[0])
   
    if not function_responses: # check if list is empty and thrown an Exception
        raise Exception("no function responses generated, exiting.")

    messages.append(types.Content( # generate the dialog with the agent
        role="user",
        parts=function_responses 
    ))

# responsible to call the functions in availabe functions 
def call_function(function_call_part, verbose=False): # function_call_part is a types.FunctionCall
    
    function_name = function_call_part.name 
    function_args = function_call_part.args 
    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")
    
    function_map = {
        "get_files_info": get_files_info, 
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file,
    }

    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
            types.Part.from_function_response(
            name=function_name,
            response={"error": f"Unknown function: {function_name}"},
            )
        ],
    )

   
    args = dict(function_args)
    print("Args dict: ", args)
    args["working_directory"] = "./calculator"

    function_result = function_map[function_name](**args)

    print("Result: ", function_result)

    return types.Content(
        role="tool",
        parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"result": function_result},
            )
        ],
    )


if __name__ == "__main__":
    main()
