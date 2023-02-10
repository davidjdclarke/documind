from datetime import datetime
import streamlit as st

from documind.engine import DocumindEngine
from documind.prompt import Prompt
from documind.utils import convert_pdf_to_txt, save_json, save_bytes


LOG_PATH = "./tmp/log.txt"


def log(message: str):
    with open(LOG_PATH, "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n{message}\n\n")


class StreamlitRunner:
    def __init__(self, engine: DocumindEngine):
        self.engine: DocumindEngine = engine

    def run(self):
        st.set_page_config(page_title="docuMIND", page_icon="resources/icon.png")
        st.markdown("**DISCLAIMER: All data used in this demo is synthetic.**")
        st.image("resources/logo.png", width=200)
        upload_file = st.file_uploader("", type=["pdf", "txt"])
        submit_button = st.button("Upload Document")

        if submit_button:
            if upload_file is not None and "document" not in st.session_state:
                st.session_state.questions = []
                st.session_state.responses = []
                st.session_state.costs = []

                if upload_file.name.endswith(".pdf"):
                    filename = f"tmp/{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}-{upload_file.name}"
                    save_bytes(filename, upload_file.getvalue())
                    st.session_state.document_content = convert_pdf_to_txt(
                        filename
                    ).replace("$", "\$")
                else:
                    st.session_state.document_content = (
                        upload_file.getvalue().decode("utf-8").replace("$", "\$")
                    )
                st.session_state.tokens = self.engine.get_tokens(
                    st.session_state.document_content
                )
                st.session_state.document_name = upload_file.name
            else:
                st.write("No file uploaded")

        if "document_content" in st.session_state:
            with st.expander(st.session_state.document_name):
                st.write(st.session_state.document_content)
            key = 0
            st.caption(f"Tokens in document: {st.session_state.tokens}")
            for q, a in zip(st.session_state.questions, st.session_state.responses):
                st.text_input("", q, key=f"question_{key}")
                st.write(a, key=f"answer_{key}")
                st.caption(
                    f"request: {round(st.session_state.costs[key], 2)} \u00A2 (total: {round(sum(st.session_state.costs), 2)} \u00A2)"
                )
                st.radio("", ["Correct", "Incorrect"], key=f"radio_{key}")
                key += 1

            question = st.text_input("", key=f"question_{key}")
            if st.button("Ask", key=f"ask_button_{key}"):
                st.session_state.questions.append(f"{question}")
                log("question: " + question)
                question = question.split("**")
                response, cost = self.engine.process(
                    document=st.session_state.document_content,
                    question=question[0],
                    max_tokens=int(question[1]) if len(question) > 1 else 100,
                )
                log("response: " + response)
                st.session_state.responses.append(f"{response}")
                st.session_state.costs.append(cost)
            if st.button("Export", key="export"):
                export = {
                    "title": st.session_state.document_name,
                    "content": st.session_state.document_content,
                    "questions": st.session_state.questions,
                    "responses": st.session_state.responses,
                }
                save_json(
                    f"logs/{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}-{st.session_state.document_name}.json",
                    export,
                )
