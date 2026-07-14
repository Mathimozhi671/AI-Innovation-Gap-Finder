from fastapi import APIRouter, Query
from services.semantic_scholar import search_papers

router = APIRouter(prefix="/search", tags=["Search"])


@router.get("/papers")
async def papers(query: str = Query(...)):
    results = await search_papers(query)

    return {
        "query": query,
        "papers": results
    }