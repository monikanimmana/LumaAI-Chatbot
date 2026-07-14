from fastapi import FastAPI  ,UploadFile , File   #type:ignore
from .routes.chat import router #type:ignore
import os
import shutil
from .rag import index_pdf
from .schemas import ChatRequest
from .vector_store import semantic_search
from .services.llm_service import stream_llm , chat
from fastapi.responses import StreamingResponse #type:ignore
 
app=FastAPI()

app.include_router(router)

@app.post("/upload")
async def upload_pdf(file:UploadFile = File(...)):
    os.makedirs("app/documents",exist_ok=True)
    file_path=f"app/documents/{file.filename}"

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    index_pdf(file_path)

    return {"message": "PDF indexed successfully"}

@app.post('/chat')
def chat_endpoint(request: ChatRequest):
    return StreamingResponse(
        chat(
            request.conversation_id,
            request.prompt
        ),
        media_type="text/plain"
    )



