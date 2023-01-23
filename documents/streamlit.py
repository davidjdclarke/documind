import streamlit as st

from documents.openai import OpenAIConnector
from documents.prompt import Prompt
from documents.utils import read_text_file, convert_pdf_to_txt


class StreamlitRunner:
    def __init__(self, open_ai_connector: OpenAIConnector):
        self.openai_connector = open_ai_connector

    def run(self):
        st.title("AI Document Processor")
        upload_file = st.file_uploader("")
        submit_button = st.button("Upload Document")

        if submit_button:
            if upload_file is not None and "document" not in st.session_state:
                st.session_state.questions = []
                st.session_state.responses = []

                if upload_file.name.endswith(".pdf"):
                    st.session_state.document = convert_pdf_to_txt(
                        upload_file.getvalue()
                    )
                else:
                    st.session_state.document = upload_file.getvalue().decode("utf-8")
            else:
                st.write("No file uploaded")

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
                # response = self.openai_connector.complete(
                #     Prompt.format_question_prompt(st.session_state.document, question),
                #     max_tokens=100,
                # )
                st.session_state.responses.append(f"{response}")
