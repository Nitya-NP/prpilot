# PRPilot 🤖

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)
![Groq](https://img.shields.io/badge/AI-Groq%20Llama3-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

AI-powered GitHub bot that automatically reviews pull requests using Llama3 via Groq. Opens a PR, get a structured code review in seconds.

![PRPilot Demo](demo.gif)

## Features

- **Automatic code review** on every PR opened
- **Bug detection** — spots common errors and issues
- **Suggestions** — best practices and improvements
- **Positives** — highlights what was done well
- **Fast** — review posted in under 10 seconds
- **CI/CD** — runs via GitHub Actions automatically

## Tech Stack

| Layer | Technology |
|---|---|
| AI Model | Llama3 via Groq API |
| Backend | FastAPI + Python |
| GitHub Integration | PyGithub + Webhooks |
| CI/CD | GitHub Actions |
| Deployment | Render |

## How It Works

1. Developer opens a pull request
2. GitHub sends webhook event to PRPilot server
3. PRPilot fetches the code diff via GitHub API
4. Diff sent to Llama3 for analysis
5. Structured review posted as PR comment

## Example Review

🤖 PRPilot Code Review
Issues Found
- Missing null check on line 12

Suggestions
- Add type hints to function parameters
- Extract logic into helper function

Positives
- Clean, readable code structure
- Good naming conventions

Summary
- Well structured code with minor improvements needed.

## Local Setup

```bash
# Clone the repo
git clone https://github.com/Nitya-NP/prpilot.git
cd prpilot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your API keys to .env

# Run the server
uvicorn app.main:app --reload --port 8000
```
## How to Get a Code Review

Every time you want PRPilot to review your code:

```bash
# Step 1 — Create a new branch
git checkout -b feature/your-feature-name

# Step 2 — Write your code, then commit
git add .
git commit -m "describe what you built"
git push origin feature/your-feature-name
```

# Step 3 — Open PR on GitHub
1. Go to github.com/Nitya-NP/prpilot
2. Click "Compare & pull request"
3. Click "Create pull request"
4. Wait 10 seconds — bot posts review automatically!

Built with by [Nitya Patel](https://github.com/Nitya-NP) - [LinkedIn](https://www.linkedin.com/in/nitya-patel-838072301/) | [Portfolio](https://nityapatel-portfolio.vercel.app/)

