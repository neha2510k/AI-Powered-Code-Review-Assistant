import requests
from app.config.settings import GITHUB_TOKEN

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

response = requests.get(
    "https://api.github.com/user/repos",
    headers=headers
)

print("Status Code:", response.status_code)

repositories = response.json()

print("\nYour Repositories:\n")

for repo in repositories:
    print(f"Repository Name : {repo['name']}")
    print(f"Private         : {repo['private']}")
    print(f"Language        : {repo['language']}")
    print("-" * 40)