import ollama #type:ignore
from ..vector_store import semantic_search
from ..chat_manager import get_conversation


def stream_llm(conversation_id:str , question:str,content:str):

    messages= get_conversation(conversation_id)
    llm_messages = messages.copy()

    llm_messages.append({
        "role":"user",
        "content": f"""

    "context":
    {content},
    "question":
    {question},

    answer=
    """
    
    })
    
    stream = ollama.chat(
        model="qwen3",
        messages=llm_messages,
        stream=True
    )

    answer=""

    for chunk in stream:
        text=chunk["message"]["content"]
        answer+=text
        yield text

 # Store only the conversation, not the retrieved context
    messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

###### Helper Function for fast semantic search #####

def build_search_query(conversation_id : str , question:str):

    messages=get_conversation(conversation_id)

    history=[]

    for msg in messages[-4:]:
        
        if(msg["role"]!= "system"):
            history.append(f"{msg["role"]}: {msg["content"]}")

    history.append(f"user: {question}")

    return "\n".join(history)


def chat(conversation_id: str , question: str ):

    get_conversation(conversation_id)
    
    search_query = build_search_query(conversation_id,question)

    chunks = semantic_search(search_query)

    context = "\n\n".join(chunks)

    return stream_llm(
        conversation_id,
        question,
        context
    )

   