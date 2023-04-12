import streamlit as st
import os

from knowledge_gpt.components.faq import faq


def set_openai_api_key(api_key: str):
    st.session_state["OPENAI_API_KEY"] = api_key


def sidebar():
    with st.sidebar:
        set_openai_api_key(os.environ.get("OPENAI_API_KEY", ""))

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖KnowledgeGPT allows you to ask questions about your "
            "documents and get accurate answers with instant citations. "
        )
        st.markdown(
            "This tool is a work in progress. "
            "You can contribute to the project on [GitHub](https://github.com/mmz-001/knowledge_gpt) "  # noqa: E501
            "with your feedback and suggestions💡"
        )
        st.markdown("Made by [mmz_001](https://twitter.com/mm_sasmitha)")
        st.markdown("---")

        faq()
