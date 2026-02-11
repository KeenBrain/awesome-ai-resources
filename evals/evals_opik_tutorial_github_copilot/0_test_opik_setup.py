import os
from dotenv import load_dotenv
load_dotenv()

# Check Opik
opik_key = os.getenv("OPIK_API_KEY")
print(f"✓ Opik API key: {opik_key[:10]}..." if opik_key else "✗ Opik API key missing!")

# Check GitHub Token
github_token = os.getenv("GITHUB_TOKEN")
print(f"✓ GitHub Token: {github_token[:10]}..." if github_token else "✗ GitHub Token missing!")

print("\n🎉 Setup complete! You're ready to go." if (opik_key and github_token) else "\n⚠️  Fix missing keys above.")
