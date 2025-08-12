import os
import sys 
from google import genai 
from dotenv import load_dotenv

def main():
    if len(sys.argv) < 2:
        print("Usage: main.py 'your_prompt here'")
        sys.exit(1)

    answer = sys.argv[1]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)


    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=answer
    )

    print(response.text)
    
    metadata = response.usage_metadata

    print(f"Prompt tokens: {metadata.prompt_token_count}")
    print(f"Response tokens: {metadata.candidates_token_count}")



if __name__ == "__main__":
    main()
