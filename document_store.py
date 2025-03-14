from haystack.document_stores import FAISSDocumentStore
from haystack.utils import convert_files_to_docs

# Step 1: Create/load document store
document_store = FAISSDocumentStore(
    sql_url="sqlite:///knowledge.db",
    embedding_dim=768,
    faiss_index_factory_str="Flat"
)

# Step 2: Convert files to Haystack documents
def process_documents():
    # Add your PDFs/TXT files to the 'data' folder first!
    docs = convert_files_to_docs(
        dir_path="data",
        split_paragraphs=True,
        split_length=150
    )
    
    # Write to database
    document_store.write_documents(docs)
    print(f"Added {len(docs)} documents to the database.")

if __name__ == "__main__":
    process_documents()