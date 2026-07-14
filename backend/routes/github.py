from fastapi import APIRouter, Query
from services.github_search import search_github
from services.innovation_engine import generate_analysis
from services.openrouter_service import analyze_innovation

router = APIRouter(prefix="/github", tags=["GitHub"])


@router.get("/search")
async def github_search(query: str = Query(...)):
    repos = search_github(query)

    ai_result = analyze_innovation(query, repos)

    return {
        "query": query,
        "repositories": repos,
        "ai_analysis": ai_result
    }