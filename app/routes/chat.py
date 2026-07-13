from fastapi import APIRouter #type:ignore
from ..schemas import ChatRequest
from ..services.llm_service import stream_llm
from fastapi.responses import StreamingResponse #type:ignore

router= APIRouter()

@router.post("/chat")
def chat(req: ChatRequest):

    return StreamingResponse(
        stream_llm(req.prompt),
        media_type="text/plain"
    )