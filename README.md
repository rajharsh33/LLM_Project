Llama2 Document Assistant

Project : Made a chatbot based on Llama 2 which answers based on the pdf shown to it. The Chatbot is deployed on Flask

Project Steps:
1. We have shown the usage as a medical chatbot but the logic can be extended to use it in any other domain for helping in reading pdfs.
2. Read the pdf using pypdf .
3. Text chunking done using Langchain
4. Created embeddings using the hugging face's transformer : sentence-transformers/all-MiniLM-L6-v
5. Stored the embeddings in Pinecone
6. Made a prompt using Langchain and fed to Llama 2 model to find similarity (cosine similarity) in the embeddings created
7. The output is based on the top 2 most similar chunks and generated using the Llama 2
8. Deployed this on Flask where the front end runs.