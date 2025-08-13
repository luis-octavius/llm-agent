import os
import sys 
from google import genai 
from google.genai import types
from dotenv import load_dotenv

def main():
    if len(sys.argv) < 2:
        print("Usage: main.py 'your_prompt here'")
        sys.exit(1)

    print("Sys argvs: ", sys.argv)
    user_prompt = sys.argv[1]


    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )

    print(response.text)

    metadata = response.usage_metadata

    if "--verbose" in sys.argv:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {metadata.prompt_token_count}")
        print(f"Response tokens: {metadata.candidates_token_count}")
   

if __name__ == "__main__":
    main()
