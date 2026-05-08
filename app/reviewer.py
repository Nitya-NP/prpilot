import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

REVIEW_PROMPT = """You are a senior software engineer doing a code review.
Analyze the following code diff and provide a structured review.

Format your response exactly like this:

## 🤖 PRPilot Code Review

### Issues Found
- List any bugs, errors, or serious problems
- If none, write "No critical issues found"

### Suggestions
- List improvements, refactoring ideas, or best practices
- If none, write "No suggestions"

### Positives
- List what was done well
- If none, write "Nothing to note"

### Summary
One sentence overall verdict.

---
*Reviewed by PRPilot 🤖 powered by Groq + Llama3*
"""

def review_code(diff: str) -> str:
    """
    Sends the code diff to Llama3 via Groq
    and returns a structured review.
    """
    if not diff.strip():
        return "No code changes found to review."

    # Truncate if diff is too long
    if len(diff) > 8000:
        diff = diff[:8000] + "\n... (truncated)"

    print("🤖 Sending diff to Groq + Llama3...")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": REVIEW_PROMPT
            },
            {
                "role": "user",
                "content": f"Please review this code diff:\n\n{diff}"
            }
        ],
        temperature=0.3
    )

    review = response.choices[0].message.content
    print("Review generated!")
    return review