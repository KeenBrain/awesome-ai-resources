"""
hello_opik.py - Your very first Opik trace
"""
import os
from dotenv import load_dotenv
load_dotenv()

# Step 1: Configure Opik
import opik
opik.configure(api_key=os.getenv("OPIK_API_KEY"))

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