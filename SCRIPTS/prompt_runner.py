"""
AtapDigital AI Prompt Library — Prompt Runner
Run Claude API untuk eksekusi prompt dari file .md
"""

import os
import sys
import re
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment
load_dotenv()

# Initialize client
client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    base_url=os.getenv("ANTHROPIC_BASE_URL")
)


def extract_variables(content: str) -> dict:
    """
    Extract all variables from prompt template.
    Variables format: {{variable_name}}
    """
    pattern = r'\{\{(\w+)\}\}'
    variables = re.findall(pattern, content)
    return {var: input(f"Enter {var}: ") for var in variables}


def load_prompt_template(file_path: str) -> str:
    """Load prompt from markdown file."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {file_path}")

    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def replace_variables(content: str, variables: dict) -> str:
    """Replace {{variable}} placeholders with actual values."""
    for key, value in variables.items():
        content = content.replace(f'{{{{{key}}}}}', value)
    return content


def extract_system_prompt(content: str) -> tuple:
    """
    Extract system prompt from markdown.
    Format:
    [SYSTEM]:
    Your system prompt here

    [USER]:
    Your user prompt here
    """
    system_match = re.search(r'\[SYSTEM\]:(.*?)\[USER\]:', content, re.DOTALL)
    user_match = re.search(r'\[USER\]:(.*)', content, re.DOTALL)

    system_prompt = system_match.group(1).strip() if system_match else ""
    user_prompt = user_match.group(1).strip() if user_match else content

    return system_prompt, user_prompt


def extract_text_from_response(response) -> str:
    """Extract text from API response, handling different block types."""
    for block in response.content:
        if hasattr(block, 'text'):
            return block.text
    return ""


def run_prompt(
    prompt_file: str,
    context: dict = None,
    model: str = "claude-sonnet-4-20250514",
    max_tokens: int = 4096
) -> str:
    """
    Execute a prompt file with Claude API.

    Args:
        prompt_file: Path to .md prompt file
        context: Dict of variables to replace in prompt
        model: Claude model to use
        max_tokens: Max response tokens

    Returns:
        Claude's response as string
    """
    # Load and prepare prompt
    content = load_prompt_template(prompt_file)

    # Extract system and user prompts
    system_prompt, user_prompt = extract_system_prompt(content)

    # Replace variables if provided
    if context:
        user_prompt = replace_variables(user_prompt, context)

    # Make API call
    print(f"Running prompt: {Path(prompt_file).name}")
    print("-" * 50)

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system_prompt if system_prompt else None,
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )

    return extract_text_from_response(response)


def run_prompt_interactive(prompt_file: str):
    """Run prompt with interactive variable input."""
    content = load_prompt_template(prompt_file)

    # Extract variables
    pattern = r'\{\{(\w+)\}\}'
    variables = {}

    if re.search(pattern, content):
        print("Please provide the following information:\n")
        for var in re.findall(pattern, content):
            variables[var] = input(f"  {var}: ")

    # Run with variables
    result = run_prompt(prompt_file, context=variables)

    # Print result
    print("\n" + "=" * 50)
    print("OUTPUT:")
    print("=" * 50)
    print(result)

    return result


def save_output(output: str, filename: str = None):
    """Save output to file."""
    if not filename:
        filename = f"output_{Path(__file__).parent.parent}/EXAMPLES/sample_outputs/output.txt"

    Path(filename).parent.mkdir(parents=True, exist_ok=True)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"\nOutput saved to: {filename}")


# CLI Interface
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("""
AtapDigital AI Prompt Library — CLI

Usage:
  python prompt_runner.py <prompt_file> [options]

Options:
  --save          Save output to file
  --model MODEL   Use specific model (default: claude-sonnet-4-20250514)

Examples:
  python prompt_runner.py ../PROMPTS/01_competitor_research/analyze_competitor.md
  python prompt_runner.py ../PROMPTS/02_content_strategy/generate_ideas.md --save
        """)
        sys.exit(1)

    prompt_file = sys.argv[1]
    save_output_flag = "--save" in sys.argv
    model = "claude-sonnet-4-20250514"

    # Check for custom model
    if "--model" in sys.argv:
        idx = sys.argv.index("--model")
        if idx + 1 < len(sys.argv):
            model = sys.argv[idx + 1]

    try:
        result = run_prompt_interactive(prompt_file)

        if save_output_flag:
            save_output(result)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
