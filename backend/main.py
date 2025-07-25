from fastapi import FastAPI
from api import article, rights, faq, chatbot, summary

app = FastAPI()

app.include_router(article.router, prefix="/api/article")
app.include_router(rights.router, prefix="/api/rights")
app.include_router(faq.router, prefix="/api/faq")
app.include_router(chatbot.router, prefix="/api/chatbot")
app.include_router(summary.router, prefix="/api/summary")
