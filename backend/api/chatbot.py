from fastapi import APIRouter
from models.schemas import ChatRequest, ChatResponse
from services.openai_client import get_chat_response

router = APIRouter()

@router.post("")
def ask_chatbot(request: ChatRequest) -> ChatResponse:
    answer = get_chat_response(request.question)
    return ChatResponse(answer=answer)