from sentence_transformers import SentenceTransformer #type:ignore

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embed(text:str):

    embedding = model.encode(text)

    return embedding

