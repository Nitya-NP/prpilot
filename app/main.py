import hmac
import hashlib
import os
from fastapi import FastAPI, Request, HTTPException
from dotenv import load_dotenv

load_dotenv()
app=FastAPI()

WEBHOOK_SECRET= os.getenv("GITHUB_WEBHOOK_SECRET")

def verify_signature(payload: bytes, signature: str) -> bool:
    if not signature:
        return False
    mac = hmac.new(
        WEBHOOK_SECRET.encode(),
        payload,
        hashlib.sha256
    )
    expected = "sha256=" + mac.hexdigest()
    return hmac.compare_digest(expected, signature)

@app.get("/")
async def root():
    """Health check — lets you confirm the server is running."""
    return {"status": "PRPilot is running 🚀"}

@app.post("/webhook")
async def webhook(request: Request):
    """
    GitHub calls this endpoint every time a PR is opened.
    Step 1: verify it's real
    Step 2: parse the event
    Step 3: print what we received (AI review comes in Phase 3)
    """
    # Get raw body and signature
    payload = await request.body()
    signature = request.headers.get("X-Hub-Signature-256", "")

    # Verify it came from GitHub
    if not verify_signature(payload, signature):
        raise HTTPException(status_code=401, detail="Invalid signature")

    # Parse the JSON body
    data = await request.json()
    event = request.headers.get("X-GitHub-Event", "unknown")

    # Only care about pull request events for now
    if event == "pull_request":
        action = data.get("action")
        pr_number = data["pull_request"]["number"]
        pr_title = data["pull_request"]["title"]
        repo_name = data["repository"]["full_name"]

        print(f"\n{'='*50}")
        print(f" PR Event received!")
        print(f" Repo:   {repo_name}")
        print(f" PR #:   {pr_number}")
        print(f" Title:  {pr_title}")
        print(f" Action: {action}")
        print(f"{'='*50}\n")

        # Only review when PR is opened or new code is pushed
        if action in ["opened", "synchronize"]:
            from app.github_helper import get_pr_diff, post_review_comment
            from app.reviewer import review_code

            print("📥 Fetching diff...")
            diff = get_pr_diff(repo_name, pr_number)

            print("🤖 Reviewing code...")
            review = review_code(diff)

            print("💬 Posting comment to PR...")
            post_review_comment(repo_name, pr_number, review)

            print("✅ Done!")

    return {"status": "received", "pr": pr_number}