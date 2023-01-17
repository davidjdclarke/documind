from documents.openai import OpenAIConnector
from documents.prompt import Prompt

from documents.utils import read_text_file, save_json


OPENAI_API_KEY = "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"


if __name__ == "__main__":
    # Create an OpenAI connector and load the questions
    openai_connector = OpenAIConnector(OPENAI_API_KEY)
    prompt_reader = Prompt("resources/questions.json")

    # Read the documents
    input_document = read_text_file("data/anon_1.txt")

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
