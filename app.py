# Create a streamlit app that allows the user to enter a question and get a response from GPT-3
import os
import sys
from load_dotenv import load_dotenv


import streamlit as st

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)
load_dotenv(".env")

from documents.streamlit import StreamlitManager
from documents.openai import OpenAIConnector


if __name__ == "__main__":
    openai_connector = OpenAIConnector(os.environ.get("OPENAI_API_KEY"))
    streamlit_manager = StreamlitManager(openai_connector)

    streamlit_manager.run()
