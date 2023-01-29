import os
import sys
from load_dotenv import load_dotenv

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)
load_dotenv(".env")

from documents.openai import OpenAIConnector
from documents.prompt import Prompt
from documents.utils import read_file

# Load the environment variables
load_dotenv(".env")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if __name__ == "__main__":
    # Create an OpenAI connector and load the questions
    openai_connector = OpenAIConnector(OPENAI_API_KEY)
    prompt_reader = Prompt("resources/questions.json")

    # Read the documents
    input_document = read_file("data/anon_1.txt")

    while 1:
        question = input(">>> ")
        response = openai_connector.complete(
            Prompt.format_question_prompt(input_document, question),
            max_tokens=100,
        )
        print(f"\n\nGPT-3: {response}\n\n")
