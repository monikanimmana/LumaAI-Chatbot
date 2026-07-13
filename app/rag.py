from pypdf import PdfReader # type:ignore
from langchain_text_splitters import RecursiveCharacterTextSplitter #type:ignore
from .embeddings import create_embed
from .vector_store import collection

def read_pdf(file_path:str)->str:
    reader=PdfReader(file_path)

    text=""

    for page in reader.pages:
        page_text=page.extract_text()

        print(page_text)

        if page_text:
            text+=page_text + "\n"

    return text

def create_chunk(text:str):

    splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    return splitter.split_text(text)

def index_pdf(file_path:str):

    text=read_pdf(file_path)

    chunks=create_chunk(text)

    embeddings= [create_embed(chunk).tolist() for chunk in chunks]

    collection.add(

        ids=[str(ids) for ids in range(len(chunks))],
        documents=chunks,
        embeddings=embeddings

    )


