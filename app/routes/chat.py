from fastapi import APIRouter #type:ignore
from ..schemas import ChatRequest
from ..services.llm_service import stream_llm
from fastapi.responses import StreamingResponse #type:ignore
from ..vector_store import semantic_search
from ..embeddings import create_embed

router= APIRouter()

@router.post("/chat")
def chat(req: ChatRequest):
    return StreamingResponse(
        chat(
            req.conversation_id,
            req.prompt
        ),
        media_type="text/plain"
    )