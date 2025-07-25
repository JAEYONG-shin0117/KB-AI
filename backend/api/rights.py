from fastapi import APIRouter

router = APIRouter()

@router.get("")
def list_rights():
    return [{"id": 1, "title": "프라이버시 보호"}]