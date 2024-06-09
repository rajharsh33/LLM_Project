from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
from langchain_pinecone import PineconeVectorStore
import os

import os
os.environ['PINECONE_API_KEY'] = "f284c621-335b-4a06-8614-0df7def26671"

index_name="financechatbot"

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


#Creating Embeddings for Each of The Text Chunks & storing
docsearch=PineconeVectorStore.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)



#If we already have an index we can load it like this
docsearch=PineconeVectorStore.from_existing_index(index_name, embeddings)