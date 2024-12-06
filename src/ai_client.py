# ai_client.py

import openai
from mistralai import Mistral
import logging

class AIClient:
    """Base class for AI clients. This can be extended to add other AI providers."""
    def get_response(self, prompts) -> str:
        """Generates a response for the given prompts."""
        raise NotImplementedError("This method should be implemented by subclasses.")


class OpenAIClient(AIClient):
    """OpenAI implementation of the AI client."""
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key

    def get_response(self, prompts) -> str:
        """Generates a response using OpenAI's GPT models."""
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=prompts
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logging.error(f"OpenAI API error: {e}")
            raise Exception("Failed to generate a response from OpenAI.")

class MistralAIClient(AIClient):
    """MistralAI implementation of the AI client."""
    def __init__(self, api_key: str, model: str = "mistral-large-latest"):
        self.api_key = api_key
        self.model = model
        self.client_mistral = Mistral(api_key=api_key)
        
    def get_response(self, prompts ) -> str:
        """Generates a response using MistralAI models."""
        try:
            response = self.client_mistral.chat.complete(
                model=self.model,
                messages=prompts
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logging.error(f"MistralAI API error: {e}")
            raise Exception("Failed to generate a response from MistralAI.")
