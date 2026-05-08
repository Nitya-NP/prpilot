import os
from app.github_helper import get_pr_diff, post_review_comment
from app.reviewer import review_code

# GitHub Actions provides these automatically
repo_name = os.getenv("GITHUB_REPOSITORY")
pr_number = int(os.getenv("PR_NUMBER"))

print(f"🔔 Reviewing PR #{pr_number} in {repo_name}")

print("📥 Fetching diff...")
diff = get_pr_diff(repo_name, pr_number)

print("🤖 Reviewing code...")
review = review_code(diff)

print("💬 Posting comment...")
post_review_comment(repo_name, pr_number, review)

print("✅ Done!")
