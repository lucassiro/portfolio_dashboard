import streamlit as st
import streamlit.components.v1 as components

st.title("Computer vision")

# st.sidebar.title("Pages")
st.title("Image classification")
st.markdown("## Cats and Dogs")

components.html(
    """
    <a target="_blank" href="https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/model_monitoring/model_monitoring.ipynb">
      <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
    </a>
    """
)

st.markdown(
    """In this project, vamos construir
    um modelo bla bla bla"""
)