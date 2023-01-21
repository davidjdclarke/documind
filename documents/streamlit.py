import streamlit as st

from documents.openai import OpenAIConnector
from documents.prompt import Prompt
from documents.utils import read_text_file


class StreamlitRunner:
    def __init__(self, open_ai_connector: OpenAIConnector):
        self.openai_connector = open_ai_connector

    def run(self):
        document_input = st.text_input("Document Path", "data/anon_1.txt")
        submit_button = st.button("Submit Document", key="submit_button")

        if submit_button:
            st.session_state.questions = []
            st.session_state.responses = []
            st.session_state.document = read_text_file(document_input)

        if "document" in st.session_state:
            st.write(st.session_state.document)
            key = 0
            for q, a in zip(st.session_state.questions, st.session_state.responses):
                st.text_input("", q, key=f"question_{key}")
                st.write(a, key=f"answer_{key}")
                key += 1

            question = st.text_input("", key=f"question_{key}")
            if st.button("Ask", key=f"ask_button_{key}"):
                st.session_state.questions.append(f"{question}")
                response = self.openai_connector.complete(
                    Prompt.format_question_prompt(st.session_state.document, question),
                    max_tokens=100,
                )
                st.session_state.responses.append(f"{response}")
