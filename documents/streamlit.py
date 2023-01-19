import streamlit as st


from documents.openai import OpenAIConnector
from documents.prompt import Prompt
from documents.utils import read_text_file


class StreamlitManager:
    def __init__(self, open_ai_connector: OpenAIConnector):
        self.question_id = 0
        self.text_id = 0
        self.open_ai_connector = open_ai_connector
        self.document = ""

    def generate_qa_block(self):
        self.question_id += 1
        question = st.text_input("", key=f"question_{self.question_id}")
        if st.button("Ask", key=f"button_{self.question_id}"):
            # _ = self.open_ai_connector.complete(
            #     Prompt.format_question_prompt(question), max_tokens=100
            # )
            st.write(question)

    @st.cache
    def load_document(self, document_path):
        return read_text_file(document_path)

    def run(self):
        st.title("Doc AI")
        document_path = st.text_input(
            "Document Path", "data/anon_1.txt", key="doc_path"
        )
        button = st.button("Load Document", key="load_doc")
        while 1:
            if button:
                document = self.load_document(document_path)
                st.write(document)

                self.generate_qa_block()
