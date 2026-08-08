from fastapi import APIRouter, Request
from app.services.gemini_service import review_pull_request

router = APIRouter()

@router.post("/github/webhook")
async def github_webhook(request: Request):
    event = request.headers.get("X-GitHub-Event")
    payload = await request.json()

    # Ignore GitHub ping event
    if event == "ping":
        return {"message": "Webhook verified successfully"}

    # Process only Pull Request events
    if event == "pull_request":
        pull_request_number = payload["pull_request"]["number"]

        # Change these to your repository details
        owner = "neha2510k"
        repo = "AI-Powered-Code-Review-Assistant"

        review_pull_request(owner, repo, pull_request_number)

        return {
            "message": f"AI review completed for PR #{pull_request_number}"
        }

    return {"message": f"Ignored {event} event"}