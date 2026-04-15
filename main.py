import os
from dotenv import load_dotenv
from google import genai


MODEL = "gemini-2.5-flash"
PROMPT = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."


def main():
    load_dotenv()
    gemini_api_key = os.environ.get("GEMINI_API_KEY", "")
    if not gemini_api_key:
        raise RuntimeError(
            'Required environment variable "GEMINI_API_KEY" was missing or empty!'
        )
    print(f'GEMINI_API_KEY: "{gemini_api_key}"')
    print(f'Model: "{MODEL}"')
    print(f'Prompt: "{PROMPT}"')

    client = genai.Client(api_key=gemini_api_key)
    response = client.models.generate_content(model=MODEL, contents=PROMPT)
    if not response:
        raise RuntimeError("expected response")
    print(f'Response: "{response.text}"')

    if not response.usage_metadata:
        raise RuntimeError("expected response usage metadata")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
