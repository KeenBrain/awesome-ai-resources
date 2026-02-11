"""
evaluation_demo.py - Automatically evaluate LLM outputs (GitHub Models Edition)
"""
import os
from dotenv import load_dotenv
load_dotenv()

import opik
opik.configure(api_key=os.getenv("OPIK_API_KEY"), project_name=os.getenv("OPIK_PROJECT_NAME"))

# Opik's LLM-judge metrics (Hallucination, AnswerRelevance) use litellm internally,
# which needs these env vars to authenticate with GitHub Models.
os.environ["OPENAI_API_KEY"] = os.getenv("GITHUB_TOKEN", "")
os.environ["OPENAI_API_BASE"] = "https://models.github.ai/inference"

from opik.evaluation import evaluate
from opik.evaluation.metrics import Hallucination, AnswerRelevance

from openai import OpenAI
client = OpenAI(
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.github.ai/inference",
)

# ========== THE FUNCTION WE'RE EVALUATING ==========
def answer_question(question: str, context: str) -> str:
    """A Q&A function that should answer based on context."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f"Answer using this context: {context}"},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

# ========== TEST CASES ==========
# Each test case has an input, context, and expected output
test_cases = [
    {
        "input": "What is the capital of France?",
        "context": "France is a country in Europe. Its capital is Paris.",
    },
    {
        "input": "Who invented the telephone?",
        "context": "Alexander Graham Bell patented the telephone in 1876.",
    },
    {
        "input": "What is the speed of light?",
        "context": "Water boils at 100 degrees Celsius.",  # TRICKY: irrelevant context!
    },
]

# ========== EVALUATION TASK ==========
def evaluation_task(test_case: dict) -> dict:
    """Run for each test case. Must return 'output'."""
    output = answer_question(
        question=test_case["input"],
        context=test_case["context"]
    )
    return {
        "input": test_case["input"],
        "output": output,
        "context": test_case["context"]
    }

# ========== RUN EVALUATION ==========
if __name__ == "__main__":
    print("🧪 Running evaluation on 3 test cases...")
    print("   Metrics: AnswerRelevance, Hallucination")
    print("   This may take a minute...\n")

    opik_client = opik.Opik()
    dataset = opik_client.get_or_create_dataset(name="qa-test-cases")
    dataset.insert(test_cases)

    results = evaluate(
        experiment_name="my-test-eval",
        dataset=dataset,
        task=evaluation_task,
        scoring_metrics=[
            AnswerRelevance(),  # Is the answer relevant to the question?
            Hallucination(),    # Did it make stuff up?
        ],
        task_threads=1,  # Run sequentially to avoid GitHub Models rate limits
    )

    print(f"\n{'='*50}")
    print("✅ Evaluation complete!")
    print("   Go to: https://www.comet.com/opik → Experiments")
    print("   Click 'my-test-eval' to see detailed scores")
    print("="*50)
    print("\n📊 Metric Guide:")
    print("   • AnswerRelevance (0-1): Higher = better")
    print("   • Hallucination (0-1):   Higher = MORE hallucination (bad!)")
