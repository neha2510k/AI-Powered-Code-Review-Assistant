# AI-Powered Code Review Assistant

An AI-powered application that automatically reviews GitHub Pull Requests using Google Gemini AI and posts review comments on GitHub.

## Features

- Automatic GitHub Pull Request review
- GitHub Webhook integration
- AI-generated code review using Google Gemini
- Reviews code for:
  - Bugs
  - Improvements
  - Best Practices
- Automatically posts review comments to GitHub Pull Requests

## Tech Stack

- Python
- FastAPI
- Google Gemini API
- GitHub REST API
- GitHub Webhooks
- Requests
- python-dotenv

## Project Workflow

Developer pushes code
→ GitHub Pull Request
→ GitHub Webhook
→ FastAPI
→ GitHub API fetches changed files
→ Gemini reviews code
→ AI posts review comment on GitHub

## Installation

```bash
git clone <repository-url>
cd AI-Powered-Code-Review-Assistant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GITHUB_TOKEN=your_token
GEMINI_API_KEY=your_api_key
```

Run the application:

```bash
uvicorn app.main:app --reload
```

## Future Enhancements

- Inline GitHub review comments
- Multi-repository support
- Better prompt engineering
- Deployment to cloud
- Authentication improvements

## Developer

K Neha