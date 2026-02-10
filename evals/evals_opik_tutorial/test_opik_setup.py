"""
Required Pre-requisites: Go through the README.md and set up your environment with the required API keys.

Once you are in your virtual environment and have installed the dependencies, run this script using the following command in your terminal:
- Mac/Linux: `python3 test_opik_setup.py`
- Windows: `python test_opik_setup.py`

"""
import os
from dotenv import load_dotenv
load_dotenv()

# Check Opik
opik_key = os.getenv("OPIK_API_KEY")
print(f"✓ Opik API key: {opik_key[:10]}..." if opik_key else "✗ Opik API key missing!")

# Check OpenAI  
openai_key = os.getenv("OPENAI_API_KEY")
print(f"✓ OpenAI API key: {openai_key[:10]}..." if openai_key else "✗ OpenAI API key missing!")

print("\n🎉 Setup complete! You're ready to go." if (opik_key and openai_key) else "\n⚠️  Fix missing keys above.")
