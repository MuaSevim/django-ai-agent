"""
Movie discovery tools for the AI agent system.

This module provides LangChain tools for interacting with The Movie Database (TMDB) API,
enabling agents to search for movies and retrieve detailed movie information.

Tools:
- search_movies: Search for movies by title/query
- movie_detail: Retrieve detailed information for a specific movie
"""
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool

from tmdb import client as tmdb_client


@tool
def search_movies(query: str, limit: int = 5, config: RunnableConfig = {}):
    """
    Search for movies on The Movie Database (TMDB).
    
    Args:
        query: Search term for movie title or keywords
        limit: Maximum number of results (max 25)
        config: LangChain runtime configuration with user context
        
    Returns:
        list: Movie search results with metadata (title, id, release_date, etc)
    """
    configurable = config.get('configurable') or config.get('metadata')
    user_id = configurable.get('user_id')
    response = tmdb_client.search_movie(query, raw=False)
    try:
        total_results = int(response.get("total_results"))
    except:
        total_results = -1
    if total_results == 0:
        return []
    if limit > 25:
        limit = 25
    results = response.get("results")[:limit]
    return results
    

@tool
def movie_detail(movie_id: int, config: RunnableConfig = {}):
    """
    Retrieve detailed information about a specific movie from TMDB.
    
    Args:
        movie_id: The TMDB movie ID
        config: LangChain runtime configuration with user context
        
    Returns:
        dict: Comprehensive movie information (cast, crew, ratings, etc)
    """
    configurable = config.get('configurable') or config.get('metadata')
    user_id = configurable.get('user_id')
    response = tmdb_client.movie_detail(movie_id, raw=False)
    return response


movie_discovery_tools = [
    search_movies,
    movie_detail
]