
from typing import List, Dict


def search_web(question: str, tavily_client, k: int = 5) -> List[Dict[str, str]]:
    """
    Uses Tavily to retrieve relevant snippets.

    Returns:
        [
            {
                "title": str,
                "url": str,
                "content": str
            },
            ...
        ]
    """

    response = tavily_client.search(
        query=question,
        search_depth="advanced",
        max_results=k
    )

    snippets = []

    for item in response.get("results", []):
        snippets.append({
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "content": item.get("content", "")
        })

    return snippets
