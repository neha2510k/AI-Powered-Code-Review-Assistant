import requests
from app.config.settings import GITHUB_TOKEN

OWNER = "neha2510k"
REPOSITORY = "AI-Powered-Code-Review-Assistant"

def get_pull_request_patches(pull_request_number):

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(
    f"https://api.github.com/repos/{OWNER}/{REPOSITORY}/pulls/{pull_request_number}/files",
    headers=headers
    )

    print("Status Code:", response.status_code)

    files = response.json()

    all_patches = ""

    for file in files:
        print("=" * 80)
        print("Filename :", file["filename"])
        print("Status   :", file["status"])
        print("Patch:\n")
        print(file.get("patch", "No patch available"))

        patch = file.get("patch", "")

        all_patches += f"\nFile: {file['filename']}\n"
        all_patches += patch + "\n"

        print("=" * 80)

    return all_patches
def post_pull_request_comment(pull_request_number, comment):

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    url = f"https://api.github.com/repos/{OWNER}/{REPOSITORY}/issues/{pull_request_number}/comments"

    data = {
        "body": comment
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    print("Comment Status Code:", response.status_code)