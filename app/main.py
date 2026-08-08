from fastapi import FastAPI
from app.api.github_webhook import router
from pydantic import BaseModel

app = FastAPI()
app.include_router(router)
class GreetingRequest(BaseModel):
    name: str


@app.get("/")
def root():
    return {
        "message": "Welcome to AI-Powered Code Review Assistant"
    }


@app.get("/about")
def about():
    return {
        "project": "AI-Powered Code Review Assistant",
        "version": "1.0.0",
        "developer": "K Neha"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
    
@app.post("/greet")
def greet(request: GreetingRequest):
    return {
        "message": f"Hello, {request.name}! Welcome to AI-Powered Code Review Assistant."
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "message": f"User ID is {user_id}"
    }
    
@app.get("/search")
def search(language: str = "Python", level: str = "Beginner"):
    return {
        "language": language,
        "level": level
    }