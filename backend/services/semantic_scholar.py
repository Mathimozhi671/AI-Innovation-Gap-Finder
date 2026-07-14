import httpx

BASE_URL = "https://api.semanticscholar.org/graph/v1"


async def search_papers(query: str, limit: int = 5):
    url = (
        f"{BASE_URL}/paper/search"
        f"?query={query}"
        f"&limit={limit}"
        f"&fields=title,abstract,year,authors,url"
    )

    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json().get("data", [])