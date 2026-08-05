from google import genai
from app.config.settings import GEMINI_API_KEY
from app.services.github_service import (
    get_pull_request_patches,
    post_pull_request_comment
)
client = genai.Client(api_key=GEMINI_API_KEY)
all_patches = get_pull_request_patches()

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="""
You are an expert software engineer.

Review the following code.

Give:
1. Bugs
2. Improvements
3. Best Practices

Code:
""" + all_patches
)

print(response.text)
post_pull_request_comment(response.text)