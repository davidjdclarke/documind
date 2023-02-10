import tiktoken

from typing import List, Tuple

from documind.openai import OpenAIConnector
from documind.prompt import Prompt

PRICING_MODEL = {
    "text-davinci-003": 0.02,
    "text-curie-001": 0.002,
    "text-babbage-001": 0.0005,
    "text-ada-001": 0.0004,
}


class DocumindEngine:
    def __init__(self, open_ai_connector: OpenAIConnector):
        self.openai_connector = open_ai_connector
        self.encoding = tiktoken.get_encoding("gpt2")

    def request(
        self, prompt: str, model: str = "text-davinci-003", max_tokens: int = 100
    ) -> Tuple[str, float]:
        """
        Sends a request to the OpenAI API and returns the response and the cost.

        Args:
            prompt (str): message to send to the API
            model (str): model to use. Defaults to "text-da-vinci-003".
            max_tokens (int): maximum number of tokens to return. Defaults to 100.

        Returns:
            Tuple[str, float]: response and cost of the request in cents
        """
        cost = PRICING_MODEL[model] * (self.get_tokens(prompt) + max_tokens) / 10
        response = self.openai_connector.complete(
            prompt, model=model, max_tokens=max_tokens
        )
        return response, cost

    def get_tokens(self, text: str) -> int:
        """
        Returns the number of tokens in a given text.

        Args:
            text (str): text to count tokens

        Returns:
            int: number of tokens
        """
        return len(self.encoding.encode(text))

    def get_blocks(
        self,
        text: str,
        max_tokens: int = 4097,
        prompt: str = "",
        response_tokens: int = 100,
        offset: int = 100,
    ) -> List[str]:
        """
        Splits a text into blocks of a given size.

        Args:
            text (str): text to split
            max_tokens (int, optional): Number of tokens permitted by model . Defaults to 4097.
            prompt (str, optional): _description_. Defaults to "".
            response (str, optional): _description_. Defaults to "".
            offset (int, optional): _description_. Defaults to 100.

        Returns:
            List[str]: _description_
        """
        block_size = max_tokens - len(self.encoding.encode(prompt)) - response_tokens
        num_blocks = len(text) // (block_size - offset) + 1

        blocks = []
        for i in range(num_blocks):
            start = i * (block_size - offset)
            end = start + block_size
            blocks.append(self.encoding.decode(self.encoding.encode(text)[start:end]))

        return blocks

    def _split_infrence(self, text: str, prompt: str, max_tokens: int = 4097) -> str:
        blocks = self.get_blocks(
            text, prompt=prompt, response_tokens=max_tokens, max_tokens=2000
        )
        responses = []
        cost = 0
        for block in blocks:
            response, cost = self.request(
                Prompt.format_question_prompt(block, prompt),
                max_tokens=max_tokens,
                model="text-ada-001",
            )
            cost += cost
            responses.append(response)
        return responses, cost

    def process(self, document: str, question: str, max_tokens: int = 100) -> str:
        """
        Processes a long form document and returns the answer to the question.

        Args:
            document (str): _description_
            question (str): _description_
            response_tokens (int, optional): _description_. Defaults to 100.

        Returns:
            str: _description_
        """
        prompt = Prompt.format_question_prompt(document, question)
        num_tokens = len(self.encoding.encode(prompt))

        while num_tokens >= 4097:
            responses = self._split_infrence(document, question, max_tokens=2000)
            prompt = Prompt.summarize_responses(responses)
            num_tokens = len(self.encoding.encode(prompt))
        return self.request(prompt, max_tokens=max_tokens)
