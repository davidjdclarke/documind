from typing import List, Optional

from documind.utils import read_json, save_json


class Prompt:
    """
    Engine that handles the questions and answers for the documents.  This class is responsible for reading and processing,
    the questions and answers for the documents.
    """

    @staticmethod
    def format_question_prompt(text: str, promt: str) -> str:
        return f"{text} \n\nuser: \n{promt} (as mentioned in the document, if not answered say so) \n\ndocumind: \n"

    @staticmethod
    def summarize_responses(responses: List[str]) -> str:
        merged = ""
        num_responses = len(responses)
        for i, response in enumerate(responses):
            merged += f"\n[RESPONSE {i} of {num_responses}]: \n{response}"
        return f"{merged} \n\nuser: \nsythenize the above responses into a single response (ignore responses that say the answer couldn't be found) \n\ndocumind: \n"

    @staticmethod
    def prompt_on_segment(
        segment: str,
        question: str,
        page_number: Optional[int] = 1,
        total_pages: Optional[int] = 1,
    ) -> bool:
        return f"[START: page {page_number}/{total_pages}] \n\n{segment} \n\n[END: page {page_number}/{total_pages}] \n\nuser: \nAnswer the following question/prompt (using only information present in the document segment above): '{question}'.  If the question/prompt is not addressed in this segment reply with '...' and nothing else."
