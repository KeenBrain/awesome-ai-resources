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
