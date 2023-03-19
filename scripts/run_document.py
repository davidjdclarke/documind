import os
from load_dotenv import load_dotenv

from documind.openai import OpenAIClient
from documind.prompt import Prompt
from documind.utils import read_file, save_json

# Load the environment variables
load_dotenv(".env")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


if __name__ == "__main__":
    # Create an OpenAI connector and load the questions
    openai_connector = OpenAIClient(OPENAI_API_KEY)
    prompt_reader = Prompt("resources/questions.json")

    # Read the documents
    input_document = read_file("data/anon_1.txt")

    # Generate Predictions
    answers = prompt_reader.get_questions()
    for key, question in answers.items():
        for id, content in question.items():
            print(f"Generating {key} prediction for {id}")
            answers["MIG"][id]["prediction"] = openai_connector.complete(
                Prompt.format_question_prompt(input_document, content["prompt"]),
                max_tokens=content["max_tokens"],
            )

    # Save the answers
    save_json("resources/answers_1.json", answers)
