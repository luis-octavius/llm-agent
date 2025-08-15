import os
import sys 
from google import genai 
from google.genai import types
from dotenv import load_dotenv
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.get_file_content import schema_get_file_content, get_file_content 
from functions.write_file import schema_write_file, write_file 

def main():
    # check if there is a prompt message (string) in cli call 
    if len(sys.argv) < 2:
        print("Usage: main.py 'your_prompt here'")
        sys.exit(1)

    print("Sys argvs: ", sys.argv)
    user_prompt = sys.argv[1]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents 
- Execute Python files with optional arguments
- Write or overwrite files 

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
    
    # available functions to the use of agent
    availabe_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_run_python_file,
            schema_get_file_content,
            schema_write_file,
        ]
    )

    # use the prompt in messages property 
    messages = [
        types.Content(
        role="user", 
        parts=[types.Part(text=user_prompt)]
        ),
    ]

    # generate the response, give the instructions and specify the model 
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages, 
        config=types.GenerateContentConfig(system_instruction=system_prompt, tools=[availabe_functions]), 
    )
    
    # check if cli call was made with verbose flag 
    if "--verbose" in sys.argv:
        verbose = True 

    text = response.text

    # return a list with the function calls
    calls = response.function_calls

    if calls != None:
        try:
            for function in calls:
                content = call_function(function, verbose)
                function_call_result = content.parts[0].function_response.response 
                if function_call_result and verbose:
                    print(f"-> {function_call_result}")
        except Exception as e:
            raise Exception(f'Fatal error: {e}')
    else:
        print(text)
    metadata = response.usage_metadata
    
    # if the cli call is with the flag verbose print some statistics
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {metadata.prompt_token_count}")
        print(f"Response tokens: {metadata.candidates_token_count}")
   

# responsible to call the functions in availabe functions 
def call_function(function_call_part, verbose=False): # function_call_part is a types.FunctionCall
    function_map = {
        "get_files_info": get_files_info, 
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file,
    }

    function_name = function_call_part.name 
    function_args = function_call_part.args 
    print(function_args)

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

    if verbose == True:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")
    
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
