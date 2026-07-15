from app.rag import read_pdf , create_chunk , index_pdf
from app.embeddings import create_embed 
from app.vector_store import semantic_search
from app.services.llm_service import stream_llm

# text = read_pdf("documents/python.pdf")

# print(len(text))

# chunks=create_chunk(text)

# print("Number of chunks:",len(chunks))

# print("------------------------------")

# print(chunks[0])

# if len(chunks)>1:
#     print(chunks[1])

# print(f"total_chunks:{len(chunks)}")

# for i , chunk in enumerate(chunks):

#     print(f"\n ========== Chunk {i + 1 } ====")

#     print(chunk)


# texts= "Python is High Level programming language and very easy syntax and works efficienty using djanjo for backend developers"

# embedding = create_embed(text)

# print(embedding)


# sentence = read_pdf("documents/python.pdf")

# chunk = create_chunk(sentence)

# embed = create_embed(chunk)

# store_embed(chunk , embed)

# print(get_all) # print(collection.get(include=["documents","embeddings"]))

# print(count)

# result = semantic_search("what programming langauge we are discussing about and how it is useful")

# for i , doc in enumerate(result,1):
#     print(f"\nresults {i}\n")

#     print(doc)

# index_pdf("documents/python.pdf")

# question = input("ASK: ")

# chunks = semantic_search(question)

# content = "\n\n".join(chunks)

# for token in stream_llm(question,content):
#     print(token , end=" ",flush=True)


from app.database.database import conn

print("database connected!")

