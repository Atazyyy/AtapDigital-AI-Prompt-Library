"""
Quick Test Script
Test apakah setup sudah benar dan API bisa connect
"""

import os
import sys

# Set UTF-8 encoding for Windows
sys.stdout.reconfigure(encoding='utf-8')

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
base_url = os.getenv("ANTHROPIC_BASE_URL")

print("=" * 50)
print("AtapDigital AI Prompt Library - Test")
print("=" * 50)

# Check environment
print("\nEnvironment Check:")
print(f"   API Key: {'OK' if api_key else 'MISSING'}")
print(f"   Base URL: {base_url}")

if not api_key:
    print("\nError: ANTHROPIC_API_KEY not found!")
    sys.exit(1)

# Test connection
print("\nTesting Connection...")
try:
    client = Anthropic(api_key=api_key, base_url=base_url)

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=100,
        messages=[
            {"role": "user", "content": "Hi! Reply with just 'OK Connection successful!' to confirm."}
        ]
    )

    # Handle different response types
    response_text = ""
    for block in response.content:
        if hasattr(block, 'text'):
            response_text = block.text
            break

    print(f"   Response: {response_text}")

    if "successful" in response_text.lower() or "OK" in response_text:
        print("\n" + "=" * 50)
        print("ALL TESTS PASSED!")
        print("=" * 50)
        print("\nNext Steps:")
        print("   1. Run a prompt: python SCRIPTS/prompt_runner.py")
        print("   2. Push to GitHub!")

    else:
        print("\nUnexpected response, but API is connected")

except Exception as e:
    print(f"\nError: {e}")
    print("\nTroubleshooting:")
    print("   1. Check your API key is correct")
    print("   2. Check your internet connection")
