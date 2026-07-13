import ollama #type:ignore

chat_history=[
    {
        "role":"System",
        "content":"You are a helpful AI assistant."
        "Answer ONLY using the provided context. "
        "If the answer is not present, say you don't know."
    }
]

def stream_llm(question:str,content:str):

    prompt= f"""

    context:{content}
    question:{question}
    answer:
    """

    chat_history.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    stream = ollama.chat(
        model="qwen3",
        messages=chat_history,
        stream=True
    )

    answer=""

    for chunk in stream:
        text=chunk["message"]["content"]
        answer+=text
        yield text

    chat_history.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

   