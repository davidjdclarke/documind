# Create a streamlit app that allows the user to enter a question and get a response from GPT-3
import os
import sys
from load_dotenv import load_dotenv

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)
load_dotenv(".env")

from documind.streamlit import StreamlitRunner
from documind.openai import OpenAIClient
from documind.engine import DocumindEngine


if __name__ == "__main__":
    openai_connector = OpenAIClient(os.environ.get("OPENAI_API_KEY"))
    engine = DocumindEngine(openai_connector)

    streamlit_manager = StreamlitRunner(engine)

    streamlit_manager.run()
