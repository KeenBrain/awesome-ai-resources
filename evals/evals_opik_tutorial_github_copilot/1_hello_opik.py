"""
hello_opik.py - Your very first Opik trace (GitHub Models Edition)
"""
import os
from dotenv import load_dotenv
load_dotenv()

# Step 1: Configure Opik
import opik
opik.configure(api_key=os.getenv("OPIK_API_KEY"), project_name=os.getenv("OPIK_PROJECT_NAME"))

# Step 2: Set up GitHub Models via OpenAI-compatible API
from openai import OpenAI
client = OpenAI(
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.github.ai/inference",
)

# Step 3: Add the @opik.track decorator - THIS IS THE MAGIC!
@opik.track
def ask_question(question: str) -> str:
    """Ask a question via GitHub Models and return the answer."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

# Step 4: Run it!
if __name__ == "__main__":
    print("🚀 Asking a question via GitHub Models...\n")

    answer = ask_question("What is the capital of France?")

    print(f"Question: What is the capital of France?")
    print(f"Answer: {answer}")
    print(f"\n{'='*50}")
    print("✅ Done! Now check your Opik dashboard:")
    print("   https://www.comet.com/opik → Projects")
    print("="*50)