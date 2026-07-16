import ollama #type:ignore
from ..vector_store import semantic_search
from ..database.message_manage import get_messages , save_messages


def stream_llm(conversation_id:str , question:str,content:str):

    messages= get_messages(conversation_id)
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

    answer= ""

    for chunk in stream:
        text=chunk["message"]["content"]
        answer+=text
        yield text

    save_messages(conversation_id , "user",question)
    save_messages(conversation_id,"assistent",answer)
###### Helper Function for fast semantic search #####

def build_search_query(conversation_id : str , question:str):

    messages=get_messages(conversation_id)

    history=[]

    for msg in messages[-4:]:
        
        if(msg["role"]!= "system"):
            history.append(f"{msg["role"]}: {msg["content"]}")

    history.append(f"user: {question}")

    return "\n".join(history)


def chat(conversation_id: str , question: str ):

    get_messages(conversation_id)
    
    search_query = build_search_query(conversation_id,question)

    chunks = semantic_search(search_query)

    context = "\n\n".join(chunks)

    return stream_llm(
        conversation_id,
        question,
        context
    )

   