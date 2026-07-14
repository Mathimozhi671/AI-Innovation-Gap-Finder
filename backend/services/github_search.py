import requests

GITHUB_API = "https://api.github.com/search/repositories"


def search_github(query: str):
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": 5
    }

    try:
        response = requests.get(
            GITHUB_API,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        repos = response.json().get("items", [])

        results = []

        for repo in repos:
            results.append({
                "name": repo.get("name"),
                "description": repo.get("description"),
                "stars": repo.get("stargazers_count"),
                "language": repo.get("language"),
                "forks": repo.get("forks_count"),
                "issues": repo.get("open_issues_count"),
                "updated": repo.get("updated_at"),
                "url": repo.get("html_url")
            })

        return results

    except requests.exceptions.RequestException as e:
        print("GitHub API Error:", e)
        return []