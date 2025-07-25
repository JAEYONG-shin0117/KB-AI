from fastapi import APIRouter

router = APIRouter()

@router.get("")
def get_faqs():
    return [{"question": "어디에 신고하나요?", "answer": "경찰청 사이버수사대"}]
