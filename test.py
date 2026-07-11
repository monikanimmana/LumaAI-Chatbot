from app.rag import read_pdf , create_chunk 
from app.embeddings import create_embed

text = read_pdf("documents/python.pdf")

print(len(text))

chunks=create_chunk(text)

print("Number of chunks:",len(chunks))

print("------------------------------")

print(chunks[0])

if len(chunks)>1:
    print(chunks[1])

print(f"total_chunks:{len(chunks)}")

for i , chunk in enumerate(chunks):

    print(f"\n ========== Chunk {i + 1 } ====")

    print(chunk)


texts= "Python is High Level programming language and very easy syntax and works efficienty using djanjo for backend developers"

embedding = create_embed(text)

print(embedding)