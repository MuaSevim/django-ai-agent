"""
Supervisor agent for multi-agent coordination.

This module implements a Supervisor pattern that routes user requests
to specialized agents (Document and Movie Discovery) based on intent.
The supervisor intelligently delegates tasks to the most appropriate agent.
"""
from langchain_openai import ChatOpenAI
from langgraph_supervisor import create_supervisor

from ai import agents
from ai.llms import get_openai_model


def get_supervisor(model=None, checkpointer=None):
    """
    Create a supervisor agent that coordinates multiple specialized agents.
    
    The supervisor receives user requests and routes them to either:
    - Document Assistant: for document management operations
    - Movie Discovery Assistant: for movie search and information
    
    Args:
        model: Optional LLM model specification. Defaults to gpt-4o-mini.
        checkpointer: Optional checkpointer for conversation state persistence.
        
    Returns:
        A compiled LangGraph supervisor agent.
    """
    llm_model = get_openai_model(model=model)

    return create_supervisor(
        agents=[
            agents.get_document_agent(),
            agents.get_movie_discovery_agent(),
        ],
        model=llm_model,
        prompt=(
            "You manage a document management assistant and a "
            "movie discovery assistant. Assign work to them based on user intent."
        ),
    ).compile(checkpointer=checkpointer)