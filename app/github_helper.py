import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def get_pr_diff(repo_name: str, pr_number: int) -> str:
    """
    Connects to GitHub and fetches the code diff
    from a pull request.
    
    repo_name: e.g. 'Nitya-NP/prpilot'
    pr_number: e.g. 1
    """
    # Connect to GitHub using your token
    g = Github(GITHUB_TOKEN)
    
    # Get the repo
    repo = g.get_repo(repo_name)
    
    # Get the pull request
    pr = repo.get_pull(pr_number)
    
    # Get all files changed in this PR
    files = pr.get_files()
    
    # Build a readable diff string
    diff_text = ""
    for file in files:
        diff_text += f"\n### File: {file.filename}\n"
        diff_text += f"Status: {file.status}\n"
        if file.patch:
            diff_text += f"Changes:\n{file.patch}\n"
        else:
            diff_text += "No patch available (binary file or too large)\n"
    
    return diff_text

def post_review_comment(repo_name: str, pr_number: int, review: str):
    """
    Posts the AI review as a comment on the PR.
    """
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    pr.create_issue_comment(review)
    print(f"✓ Review posted to PR #{pr_number}")