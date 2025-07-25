from fastapi import APIRouter
from services.naver_crawler import search_articles

router = APIRouter()

@router.get("/search")
def search(q: str):
    articles = search_articles(q)
    return {"results": articles}
