import logging
import concurrent.futures

from typing import Optional

from documind.document import Document
from documind.prompt import Prompt
from documind.openai import OpenAIClient


logger = logging.getLogger(__name__)


PRICING_MODEL = {
    "text-davinci-003": 0.02,
    "text-curie-001": 0.002,
    "text-babbage-001": 0.0005,
    "text-ada-001": 0.0004,
}


def get_cost(num_tokens: int, model: str = "text-davinci-003") -> float:
    return PRICING_MODEL[model] * num_tokens / 10


class Documind:
    def __init__(self, document: Document, openai: OpenAIClient):
        self.document = document
        self.openai = openai
        self.cost = []
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
        cost = get_cost(prompt_size)
        logger.info(f"Processing question with estimated cost of {cost} cents.")

        if prompt_size < 4097:
            logger.info("Single-part prompt required.")
            response = self.openai.complete(prompt, max_tokens=max_tokens)
            logger.info(f"Response: {response}")
            return response, cost

        chunks = self.document.chunk_text(
            4097 - (prompt_size - self.document.get_num_tokens(self.document.text)), 126
        )
        logger.info(f"Split document into {len(chunks)} chunks.")

        if not deep:
            for i, chunk in enumerate(chunks):
                logger.info(f"Inferencing on chunk {i+1} of {len(chunks)}")
                prompt = Prompt.format_question_prompt(chunk, question)
                response = self.openai.complete(prompt, max_tokens=max_tokens)

                if "..." not in response:
                    return response, cost

            return "No answer found.", cost

        logger.info("Deep inference enabled. Using threads. (This may take a while)")
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            logger.info("Starting threads...")
            futures = [
                executor.submit(
                    self.openai.complete,
                    Prompt.format_question_prompt(chunk, question),
                    max_tokens=max_tokens,
                )
                for chunk in chunks
            ]
            logger.info("Waiting for threads to finish...")

        logger.info("Threads finished. Processing responses...")
        return (
            self.openai.complete(
                Prompt.summarize_responses([f.result() for f in futures]),
                max_tokens=max_tokens,
            ),
            cost,
        )
