# Run a chatbot using GPT-3
import sys

ROOT_DIR = "/home/djclarke/Projects/documents"
if ROOT_DIR not in sys.path:
    sys.path.append("/home/djclarke/Projects/documents")

from documents.openai import OpenAIConnector


OPENAI_API_KEY = "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"


def run_completion(openai: OpenAIConnector):
    while 1:
        user_input = input("User: ")
        response = openai.complete(user_input)
        print(f"\n\nGPT-3: {response}\n\n")


def run_edit(openai: OpenAIConnector):
    while 1:
        user_input = input("Enter Input:\n")
        user_instructions = input("Enter Instructions:\n")
        response = openai.edit(user_input, user_instructions)
        print(f"\n\nGPT-3: {response}\n\n")


if __name__ == "__main__":
    # Create an OpenAI connector
    openai = OpenAIConnector(OPENAI_API_KEY)

    selection = input("Select an option:\n1. Completion\n2. Edit\n3. Exit\n")
    if selection == "1":
        run_completion(openai)
    elif selection == "2":
        run_edit(openai)
    elif selection == "3":
        exit()
