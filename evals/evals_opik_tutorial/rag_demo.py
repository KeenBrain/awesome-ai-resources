"""
rag_demo.py - A mini RAG pipeline with nested traces
"""
import os
from dotenv import load_dotenv
load_dotenv()

import opik
opik.configure(api_key=os.getenv("OPIK_API_KEY"))

from openai import OpenAI
client = OpenAI()

# Our "knowledge base" (in real life, this would be a vector database)
KNOWLEDGE_BASE = {
    "python": "Python was created by Guido van Rossum and released in 1991.",
    "javascript": "JavaScript was created by Brendan Eich in 1995 for Netscape.",
    "rust": "Rust was created by Mozilla employee Graydon Hoare and first released in 2010.",
}

# ========== STEP 1: RETRIEVE ==========
@opik.track(name="retrieve")
def retrieve_context(query: str) -> str:
    """Find relevant info in our knowledge base."""
    query_lower = query.lower()
    for keyword, info in KNOWLEDGE_BASE.items():
        print(f"checking keyword: {keyword}\n")
        if keyword in query_lower:
            print(f"matched with keyword: {keyword}\n")
            return info
    return "No relevant information found."

# ========== STEP 2: GENERATE ==========
@opik.track(name="generate")
def generate_answer(question: str, context: str) -> str:
    """Generate an answer using the retrieved context."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"Answer using ONLY this context: {context}\n\nIf the context doesn't help, say so."
            },
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

# ========== MAIN PIPELINE ==========
@opik.track(name="rag_pipeline")
def rag_pipeline(question: str) -> str:
    """
    The full RAG pipeline. 
    In Opik, you'll see this as a PARENT with two CHILDREN.
    """
    context = retrieve_context(question)  # Child 1
    answer = generate_answer(question, context)  # Child 2
    return answer

# ========== RUN IT ==========
if __name__ == "__main__":
    questions = [
        "Who created Python?",
        "When was JavaScript made?",
        "What is quantum computing?",  # No context for this one!
    ]
    
    for q in questions:
        print(f"\n❓ {q}")
        answer = rag_pipeline(q)
        print(f"💬 {answer}")
    
    print(f"\n{'='*50}")
    print("✅ Check Opik to see NESTED traces!")
    print("   Each rag_pipeline has retrieve + generate inside it")
    print("="*50)