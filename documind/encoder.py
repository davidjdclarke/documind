import tiktoken

from typing import List


class Encoder:
    def __init__(self, vocab: str = "gpt2"):
        self.encoder = tiktoken.get_encoding(vocab)

    def convert_to_tokens(self, text: str) -> List[int]:
        return self.encoder.encode(text)

    def convert_to_text(self, tokens: List[int]) -> str:
        return self.encoder.decode(tokens)
