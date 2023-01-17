from typing import List, Optional

from documents.utils import read_json, save_json


class Prompt:
    """
    Engine that handles the questions and answers for the documents.  This class is responsible for reading and processing,
    the questions and answers for the documents.
    """

    def __init__(self, file_path: str = "resources/questions.json"):
        self.file_path = file_path
        self.questions = read_json(self.file_path)

    def save(self, output_path: str = None):
        save_json(output_path, self.questions)

    def get_questions(self, type: Optional[str] = None) -> List:
        if type is None:
            return self.questions
        return self.questions[type]

    @staticmethod
    def format_question_prompt(text: str, promt: str) -> str:
        return f"{text} \n\nQ. \n{promt} \n\nA. \n"
