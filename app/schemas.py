from pydantic import BaseModel #type:ignore

class ChatRequest(BaseModel):
    conversation_id=str
    prompt:str

class ChatResponse(BaseModel):
    answer:str