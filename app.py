# Create a streamlit app that allows the user to enter a question and get a response from GPT-3
import os
import sys
from load_dotenv import load_dotenv

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)
load_dotenv(".env")

from documind.streamlit import StreamlitRunner
from documind.openai import OpenAIClient
from documind.documind import Documind
from documind.document import Document


if __name__ == "__main__":
    openai = OpenAIClient(os.environ.get("OPENAI_API_KEY"))
    document = Document("")
    engine = Documind(document, openai)

    streamlit_manager = StreamlitRunner(engine)

    streamlit_manager.run_documind()
