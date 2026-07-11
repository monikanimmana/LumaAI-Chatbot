from pydantic import BaseModel

class ChatResquest(BaseModel):
    prompt:str

class ChatResponse(BaseModel):
    answer:str