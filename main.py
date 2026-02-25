import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print("Please provie prompt")
    exit(1)

verbose = False
if "--verbose" in sys.argv:
    verbose = True
    sys.argv.remove("--verbose")

user_prompt = sys.argv[1]


messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

resp = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents=messages
)

if verbose:
    print("User prompt:", user_prompt)
    print("Prompt tokens:", resp.usage_metadata.prompt_token_count)
    print("Response tokens:", resp.usage_metadata.candidates_token_count)

print(resp.text)