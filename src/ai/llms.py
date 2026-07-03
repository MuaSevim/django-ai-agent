"""
LLM configuration and initialization utilities.

Provides factory functions for creating LangChain language model instances,
with support for configurable model selection and OpenAI API integration.
"""
from django.conf import settings
from langchain_openai import ChatOpenAI


def get_openai_api_key():
    """
    Retrieve the OpenAI API key from Django settings.
    
    Returns:
        str: The OpenAI API key configured in settings.
    """
    return settings.OPENAI_API_KEY


def get_openai_model(model: str = "gpt-4o-mini") -> ChatOpenAI:
    """
    Create a ChatOpenAI model instance with recommended settings.
    
    Args:
        model: Model identifier (e.g., 'gpt-4o', 'gpt-4o-mini'). 
               Defaults to 'gpt-4o-mini' for cost efficiency.
    
    Returns:
        ChatOpenAI: Configured language model instance.
    """
    if model is None:
        model = "gpt-4o-mini"
    return ChatOpenAI(
        model=model,
        temperature=0,
        max_retries=2,
        api_key=get_openai_api_key(), 
    )