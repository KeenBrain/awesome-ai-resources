"""
hello_opik.py - Your very first Opik trace

Required Pre-requisites: Go through the README.md and set up your environment with the required API keys.

Once you are in your virtual environment and have installed the dependencies, run this script using the following command in your terminal:
- Mac/Linux: `python3 hello_opik.py`
- Windows: `python hello_opik.py`

This is a simple demo to show how to create your first trace with Opik. The function `ask_question` is decorated with `@opik.track`, which means that every time you call this function, a new trace will be created in your Opik dashboard. This allows you to see the details of each call, including the input parameters, output, and any errors that may occur.
"""
import os
from dotenv import load_dotenv
load_dotenv()

# Step 1: Configure Opik
import opik
opik.configure(api_key=os.getenv("OPIK_API_KEY"))
os.environ["OPIK_PROJECT_NAME"] = "lets_try_evals_with_opik"

# Step 2: Set up OpenAI
from openai import OpenAI
client = OpenAI()

# Step 3: Add the @opik.track decorator - THIS IS THE MAGIC!
@opik.track
def ask_question(question: str) -> str:
    """Ask GPT a question and return the answer."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

# Step 4: Run it!
if __name__ == "__main__":
    print("🚀 Asking GPT a question...\n")
    
    answer = ask_question("What is the capital of France?")
    
    print(f"Question: What is the capital of France?")
    print(f"Answer: {answer}")
    print(f"\n{'='*50}")
    print("✅ Done! Now check your Opik dashboard:")
    print("   https://www.comet.com/opik → Projects → Your Project → Traces")
    print("="*50)