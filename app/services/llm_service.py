import ollama

chat_history=[
    {
        "role":"System",
        "content":"You are a helpful AI assistant."
    }
]

def stream_llm(prompt):

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
        yield chunk.message.content

    print()


    chat_history.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

    return answer