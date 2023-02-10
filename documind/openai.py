import random
import string
from typing import Optional

import openai


class OpenAIClient:
    def __init__(self, api_key: Optional[str] = None):
        self._api_key = api_key
        self._session_id = None
        openai.api_key = self._api_key

    def complete(
        self,
        prompt: str,
        max_tokens: int = 100,
        model: str = "text-davinci-003",
        temperature: float = 0.5,
        top_p: float = 1,
        frequency_penalty: float = 0,
        presence_penalty: float = 0,
        stop: Optional[str] = None,
    ) -> str:
        """
        Send a request to the OpenAI API and return the response.

        :param prompt: The prompt to send to the OpenAI API
        :param max_tokens: The maximum number of tokens to return
        :param temperature: Controls the 'randomnes' of the model (0 - 1)
        :param top_p: The top p value of the model
        :param frequency_penalty: The frequency penalty of the model
        :param presence_penalty: The presence penalty of the model
        :param stop: The stop sequence of the model
        """
        # Send a request to the OpenAI API
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop,
        )

        return response.choices[0].text

    def edit(
        self,
        prompt: str,
        instruction: str,
        engine: str = "text-davinci-003",
        max_tokens: int = 1024,
        temperature: float = 0.5,
        top_p: float = 1,
        frequency_penalty: float = 0,
        presence_penalty: float = 0,
        stop: Optional[str] = None,
    ) -> str:
        """
        Send a request to the OpenAI API and return the response.

        Args:
            prompt (str):
            instruction (str):
            engine (str, optional): _description_. Defaults to "text-davinci-003".
            max_tokens (int, optional): _description_. Defaults to 1024.
            temperature (float, optional): _description_. Defaults to 0.5.
            top_p (float, optional): _description_. Defaults to 1.
            frequency_penalty (float, optional): _description_. Defaults to 0.
            presence_penalty (float, optional): _description_. Defaults to 0.
            stop (Optional[str], optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        response = openai.Edit.create(
            engine=engine,
            promt=prompt,
            instruction=instruction,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop,
        )

        return response.choices[0].text
