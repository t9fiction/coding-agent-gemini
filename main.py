import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types



def main():

    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    verbose_flag = False
    
    if len(sys.argv) < 2:
        print("I need a prompt")
        sys.exit(1)
    
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True
            
    prompt = sys.argv[1]
    
    # so instead of passing prompt directly to response, we'll now do it user-message
    messages = [
        types.Content(
            role="user",
            parts=[types.Part(text=prompt)]
        )
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    if response is None or response.usage_metadata is None:
        return
    print(response.text)
    
    if verbose_flag:
        print(f"User Prompt: {prompt}")
        print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response Tokens: {response.usage_metadata.candidates_token_count}")



if __name__ == "__main__":
    main()
