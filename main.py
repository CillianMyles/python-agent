import os
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        raise RuntimeError(
            'Required environment variable "GEMINI_API_KEY" was missing or empty!'
        )
    print(f'Loaded environment variable... "GEMINI_API_KEY" --> "{gemini_api_key}"')

    client = genai.Client(api_key=gemini_api_key)
    model = "gemini-2.5-flash"
    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    print(f'Model --> "{model}"')
    print(f'Prompt --> "{prompt}"')
    response = client.models.generate_content(model=model, contents=prompt)
    print(f'Response --> "{response.text}"')


if __name__ == "__main__":
    main()
