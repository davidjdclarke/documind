import logging
import concurrent.futures

from typing import Optional

from documind.document import Document
from documind.prompt import Prompt
from documind.openai import OpenAIClient


logger = logging.getLogger(__name__)


class Documind:
    def __init__(self, document: Document, openai: OpenAIClient):
        self.document = document
        self.openai = openai

        self.responses = {}

    def process(
        self,
        question: str,
        max_tokens: int = 100,
        deep: bool = True,
        document: Optional[Document] = None,
    ) -> str:
        """
        Answer a question using the document.

        :param question: question to answer
        :param max_tokens: maximum number of tokens to return
        :param deep: whether to use deep inference
        :return: answer to the question
        """
        if document:
            self.document = document
        prompt = Prompt.format_question_prompt(self.document.text, question)
        prompt_size = self.document.get_num_tokens(prompt) + max_tokens

        if prompt_size < 4097:
            return self.openai.complete(prompt, max_tokens=max_tokens)

        # print(f"Multi-part prompt required. First prompt size: {prompt_size}")
        chunks = self.document.chunk_text(
            4097 - (prompt_size - self.document.get_num_tokens(self.document.text)), 126
        )

        if not deep:
            for i, chunk in enumerate(chunks):
                # print(f"Inferencing on chunk {i+1} of {len(chunks)}")
                prompt = Prompt.format_question_prompt(chunk, question)
                response = self.openai.complete(prompt, max_tokens=max_tokens)
                # print(f"Response: {response}")

                if "..." not in response:
                    return response, 0

            return "No answer found.", 0

        # print("Deep inference enabled. Using threads. (This may take a while)")
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [
                executor.submit(
                    self.openai.complete,
                    Prompt.format_question_prompt(chunk, question),
                    max_tokens=max_tokens,
                )
                for chunk in chunks
            ]

        # print("Threads complete. Summarizing responses.")
        # return [f.result() for f in futures]
        return (
            self.openai.complete(
                Prompt.summarize_responses([f.result() for f in futures]),
                max_tokens=max_tokens,
            ),
            0,
        )
