from fastapi import FastAPI
from local_chatbot.env.routes.chat import router

app=FastAPI()

app.include_router(router)