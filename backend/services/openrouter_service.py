import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def analyze_innovation(idea: str, repositories: list):

    repo_text = ""

    if repositories:
        for repo in repositories:
            repo_text += f"""
Repository Name: {repo.get('name')}
Description: {repo.get('description')}
Stars: {repo.get('stars')}
GitHub URL: {repo.get('url')}
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

    response = client.chat.completions.create(
        model="qwen/qwen-2.5-7b-instruct",
        messages=[
            {
                "role": "system",
                "content": "You are an expert AI innovation consultant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content