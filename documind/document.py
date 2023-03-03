import re

from typing import Optional, List

from documind.encoder import Encoder


class Document:
    def __init__(self, text: str, encoder: Optional[Encoder] = None) -> None:
        self._special_chars = re.escape("!@#$%^&*()_+-=[]{}\?.,")
        self.text = self.clean(text)

        self.encoder = encoder
        if self.encoder is None:
            self.encoder = Encoder()

        self.tokens = self.encoder.convert_to_tokens(self.text)

    @property
    def size(self) -> int:
        """
        The size of the document in characters.
        """
        return len(self.tokens)

    def clean(self, text: str) -> str:
        """
        Clean the text.

        :param text: The text to clean
        :return: The cleaned text
        """
        return re.sub(rf"[^{self._special_chars}\w\s]+", "", text)

    def get_num_tokens(self, text: str) -> int:
        """
        Get the number of tokens in a string.

        :param text: The string to get the number of tokens for
        :return: The number of tokens
        """
        return len(self.encoder.convert_to_tokens(text))

    def chunk_text(self, chunk_size: int = 1024, overlap: int = 0) -> List[str]:
        """
        Chunk the text into a list of strings.

        :param chunk_size: The size of each chunk
        :param overlap: The number of characters to overlap
        :return: A list of strings
        """
        return [
            self.encoder.convert_to_text(self.tokens[i : i + chunk_size])
            for i in range(0, len(self.tokens), chunk_size - overlap)
        ]
