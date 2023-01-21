from documents.openai import OpenAIConnector
from documents.prompt import Prompt


class Engine:
    """
    Engine that handles the questions and answers for the documents.  This class is responsible for reading and processing,
    the questions and answers for the documents.
    """

    def __init__(self, openai_connector: OpenAIConnector, prompt_reader: Prompt):
        self.openai_connector = openai_connector
        self.prompt_reader = prompt_reader
        self.document = None

    def set_document(self, document: str):
        self.document = document

    def ask(self, question: str, max_tokens: int = 100) -> str:
        return self.openai_connector.complete(
            self.prompt_reader.format_question_prompt(self.document, question),
            max_tokens=max_tokens,
        )
