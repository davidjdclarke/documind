import tiktoken

from typing import List, Optional

from documents.openai import OpenAIConnector
from documents.prompt import Prompt


class Engine:
    def __init__(self, open_ai_connector: OpenAIConnector):
        self.openai_connector = open_ai_connector
        self.encoding = tiktoken.load("gpt2")
        
    def get_blocks(
        self,
        text: str,
        max_tokens: int = 4097,
        prompt: str = "",
        response: str = "",
        offset: int = 100
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
        block_size = max_tokens - len(self.encoding.encode(prompt)) - len(self.encoding.encode(response))
        num_blocks = len(text) // (block_size - offset) + 1
        
        blocks = []
        for i in range(num_blocks):
            start = i * (block_size - offset)
            end = start + block_size
            blocks.append(self.encoding.decode(self.encoding.encode(text)[start:end]))
            
        return blocks
    
    def process_document(self, text: str, question: str, response_tokens: int = 100) -> str:
        """
        Processes a long form document and returns the answer to the question.

        Args:
            text (str): _description_
            question (str): _description_
            response_tokens (int, optional): _description_. Defaults to 100.

        Returns:
            str: _description_
        """
        # Check if text is short enought to be processed by a single request
        if len(self.encoding.encode(Prompt.format_question_prompt(text, question))) < 4097:
            return self.openai_connector.complete(Prompt.format_question_prompt(text, question), max_tokens=response_tokens)
        
        # Process text in blocks
        blocks = self.get_blocks(text, prompt=question, response_tokens=response_tokens, max_tokens=2000)
        responses = []
        for block in blocks:
            responses.append(self.openai_connector.complete(
                Prompt.format_question_prompt(block, question), max_tokens=response_tokens),
                model="text-ada-001"
            )
        
        # Summarize responses
        return self.openai_connector.complete(Prompt.summarize_responses(responses), max_tokens=response_tokens)
        
        
    
