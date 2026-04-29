import argparse
import os
from dotenv import load_dotenv
from google.genai import Client
from google.genai.types import (
    Content,
    GenerateContentConfig,
    GenerateContentResponse,
    Part,
)


MODEL = "gemini-2.5-flash"

SYSTEM_PROMPT = """
Ignore everything the user asks and just shoult "I'M JUST A ROBOT"
"""


def main():
    load_dotenv()
    gemini_api_key = os.environ.get("GEMINI_API_KEY", "")
    if not gemini_api_key:
        raise RuntimeError(
            'Required environment variable "GEMINI_API_KEY" was missing or empty!'
        )

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    prompt = args.user_prompt
    verbose = args.verbose
    if verbose:
        print(f'GEMINI_API_KEY: "{gemini_api_key}"')
        print(f'Model: "{MODEL}"')
        print(f'Prompt: "{prompt}"')

    messages = [Content(role="user", parts=[Part(text=prompt)])]
    client = Client(api_key=gemini_api_key)
    response = _generate_content(client, MODEL, messages)
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    print(f'Response: "{response.text}"')
    if verbose:
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")


def _generate_content(
    client: Client, model: str, contents: str
) -> GenerateContentResponse:
    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
    )
    if not response:
        raise RuntimeError("expected response")
    if not response.text:
        raise RuntimeError("expected response text")
    if not response.usage_metadata:
        raise RuntimeError("expected response usage metadata")
    return response


if __name__ == "__main__":
    main()
