from haystack.nodes import EmbeddingRetriever, FARMReader
from haystack.pipelines import ExtractiveQAPipeline
from document_store import document_store

# Step 1: Initialize Retriever (semantic search)
retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="sentence-transformers/all-MiniLM-L6-v2"
)

# Step 2: Initialize Reader (QA model)
reader = FARMReader(
    model_name_or_path="deepset/roberta-base-squad2",
    use_gpu=False
)

# Step 3: Create pipeline
pipeline = ExtractiveQAPipeline(reader, retriever)

# Optional: Add expert insights (run this after capturing data)
def update_embeddings():
    document_store.update_embeddings(retriever)
    print("Embeddings updated with latest data!")