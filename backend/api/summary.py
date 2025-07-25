from fastapi import APIRouter

router = APIRouter()

@router.post("")
def summarize(text: str):
    return {"summary": "이것은 요약 예시입니다."}