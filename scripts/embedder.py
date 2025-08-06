# Handling the embedding and retrieval of contract text chunks for the RAG pipeline


from sentence_transformers import SentenceTransformer  # generating text embeddings
import chromadb #vector database for storing and searching embeddings

# Loading SentenceTransformer model for converting text into embeddings
# 'all-MiniLM-L6-v2' is a lightweight, general-purpose embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')
chroma_client = chromadb.Client()


# Creating a collection named "contract_chunks"
# This will store contract text chunks and their embeddings
collection = chroma_client.get_or_create_collection("contract_chunks")

#Converting text chunks into embeddings and storing them in the ChromaDB collection
def embed_and_store_chunks(chunks):
    embeddings = model.encode(chunks)
    for i, chunk in enumerate(chunks):
        collection.add(documents=[chunk], embeddings=[embeddings[i]], ids=[f"chunk_{i}"])

# Finding the most relevant contract chunks for a given query using vector similarity
def retrieve_relevant_chunks(query, top_k=3):
    query_embedding = model.encode([query])[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    
    # Return the list of top matching chunk texts
    return results['documents'][0]