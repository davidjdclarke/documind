from typing import List, Optional

from documents.utils import read_json, save_json


class Prompt:
    """
    Engine that handles the questions and answers for the documents.  This class is responsible for reading and processing,
    the questions and answers for the documents.
    """
    @staticmethod
    def format_question_prompt(text: str, promt: str) -> str:
        return f"{text} \n\nuser: \n{promt} \n\ndocumind: \n"
    
    @staticmethod
    def summarize_responses(responses: List[str]) -> str:
        merged_responses = " ".join(responses)
        return f"Answers: \n{merged_responses} \n\nSummarize multiple answers: \n"
