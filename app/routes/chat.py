from fastapi import APIRouter
from schemas import ChatResquest
from services.llm_service import stream_llm
from fastapi.responses import StreamingResponse

router= APIRouter()

@router.post("/chat")
def chat(req: ChatResquest):

    return StreamingResponse(
        stream_llm(req.prompt),
        media_type="text/plain"
    )