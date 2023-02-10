from documind.openai import OpenAIConnector
from documind.prompt import Prompt


class FinacialProcessor:
    def __init__(self, openai_connector: OpenAIConnector) -> None:
        self._openai_connector: OpenAIConnector = openai_connector

    def process_quarterly_results(data: str):
        first_section = data[:1000]

        # get sections
        sections = (
            self._openai_connector.complete(
                Prompt.format_question_prompt(
                    st.session_state.document,
                ),
                max_tokens=int(question[1]) if len(question) > 1 else 100,
            ),
        )
