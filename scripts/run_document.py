import sys
import json

import pandas as pd

ROOT_DIR = "/home/djclarke/Projects/documents"
if ROOT_DIR not in sys.path:
    sys.path.append("/home/djclarke/Projects/documents")

from documents.openai import OpenAIConnector
from documents.questions import Questions

def read_text_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()
    
def read_json(file_path: str) -> dict:
    with open(file_path, "r") as f:
        return json.load(f)
    
def save_json(file_path: str, data: dict):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
        
def format_question_prompt(text: str, promt: str) -> str:
    return f"{text} \n\nQ. \n{promt} \n\nA. \n"
        
OPENAI_API_KEY = "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"


def answer_questions(document: str, questions: dict) -> dict:
    answers = {}
    for id, question in questions.items():
        answers[id] = openai.complete(question[0], max_tokens=question[1])
    return answers

if __name__ == "__main__":
    # Create an OpenAI connector and load the questions
    openai = OpenAIConnector(OPENAI_API_KEY)
    questions = read_json("resources/questions.json")
    
    # Read the documents
    mig = read_text_file("data/mig.txt")
    mrb = read_text_file("data/mrb.txt")
        
    # Generate MIG Predictions
    openai.start_session()
    _ = openai.complete(mig, max_tokens=1)
    for id, content in questions["MIG"].items():
        questions["MIG"][id]["prediction"] = openai.complete(format_question_prompt(mig, content["prompt"]), max_tokens=content["max_tokens"])
        
    # Generate MRB Predictions
    openai.start_session()
    _ = openai.complete(mrb, max_tokens=1)
    for id, content in questions["MRB"].items():
        questions["MRB"][id]["prediction"] = openai.complete(format_question_prompt(mrb, content["prompt"]), max_tokens=content["max_tokens"])
        
    # Save the answers
    save_json("data/answers.json", questions)
        
