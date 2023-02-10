import cohere


class CohereClient:
    def __init__(self, api_key: str):
        self._api_key = api_key
        self.client = cohere.Client(api_key)

    def complete(self, prompt: str) -> str:
        response = self.client.generate(prompt)
        return response.text
