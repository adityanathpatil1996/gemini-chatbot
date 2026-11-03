import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables or .env file.")

gemini_model = os.getenv("GEMINI_MODEL")
if not gemini_model:
    raise ValueError("GEMINI_MODEL not found in environment variables or .env file.")

client = genai.Client(api_key=api_key)


def ask_gemini(prompt: str):
    try:
        response = client.models.generate_content(
            model=gemini_model,
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"


def main():
    print("Gemini 3.8 Flash Terminal Assistant (Type 'exit' or 'quit' to stop)\n")
    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            if not user_input:
                continue

            print("\nGemini is thinking...")
            response_text = ask_gemini(user_input)
            print(f"Gemini:\n{response_text}\n" + "-" * 40)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()