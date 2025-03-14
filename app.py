import streamlit as st
from pipeline import pipeline, update_embeddings
from expert_insights import save_expert_insight

st.set_page_config(page_title="KnowledgeBridge", layout="wide")
st.title("🔍 Intelligent Knowledge Management System")

# Toggle for expert mode
expert_mode = st.sidebar.checkbox("Expert Mode")

# Chat Interface
user_query = st.text_input("Ask a question about CAD, software, or engineering:")

if user_query:
    # Get answers from documents
    results = pipeline.run(
        query=user_query,
        params={"Retriever": {"top_k": 3}, "Reader": {"top_k": 2}}
    )
    
    # Display results
    st.subheader("Answers:")
    for answer in results["answers"]:
        if answer.score > 0.1:
            st.markdown(f"**Answer**: {answer.answer}")
            st.markdown(f"**Source**: {answer.meta['name']}")
            st.markdown(f"**Confidence**: {answer.score:.2f}")
            st.markdown("---")

# Expert knowledge capture
if expert_mode:
    st.sidebar.header("Share Your Expertise")
    problem = st.sidebar.text_area("Describe the problem:")
    solution = st.sidebar.text_area("Share your solution:")
    if st.sidebar.button("Save Insight"):
        save_expert_insight(problem, solution)
        update_embeddings()  # Re-train with new data
        st.sidebar.success("Your insight has been added to the knowledge base!")