import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def analyze_innovation(idea: str, repositories: list):

    repo_text = ""

    if repositories:
        for repo in repositories:
            repo_text += f"""
Repository Name: {repo.get("name")}
Description: {repo.get("description")}
Stars: {repo.get("stars")}
GitHub URL: {repo.get("url")}

"""

    else:
        repo_text = "No GitHub repositories found."

    prompt = f"""
You are an AI Innovation Research Assistant.

Project Idea:
{idea}

Existing GitHub Projects:
{repo_text}

Analyze these repositories and provide:

1. Existing Solutions
2. Common Technologies Used
3. Common Features
4. Limitations
5. Innovation Gaps
6. Suggested Datasets
7. Suggested Algorithms
8. Recommended Tech Stack
9. Future Scope

Return the answer using headings and bullet points.
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.3,
            "max_new_tokens": 700
        }
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload
    )

    if response.status_code != 200:
        return response.text

    result = response.json()

    if isinstance(result, list):
        return result[0]["generated_text"]

    return result