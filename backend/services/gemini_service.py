import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_innovation(idea: str, repositories: list):
    """
    Analyze GitHub repositories and suggest innovation gaps.
    """

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

Analyze these repositories and provide the following:

1. Existing Solutions
2. Common Technologies Used
3. Common Features
4. Limitations
5. Innovation Gaps
6. Suggested Datasets
7. Suggested Algorithms
8. Recommended Tech Stack
9. Future Scope

Return the answer using clear headings and bullet points.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return f"Error generating AI analysis: {str(e)}"