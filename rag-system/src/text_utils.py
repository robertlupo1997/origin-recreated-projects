"""Text processing utilities for search scoring."""

def calculate_text_score(query: str, text: str) -> float:
    """Calculate similarity score between query and text."""
    query_words = set(query.lower().split())
    text_words = set(text.lower().split())
    
    if not query_words:
        return 0.0
    
    # Simple word overlap scoring
    overlap = len(query_words.intersection(text_words))
    return overlap / len(query_words)

def extract_excerpt(text: str, max_length: int = 100) -> str:
    """Extract a text excerpt of specified length."""
    if len(text) <= max_length:
        return text
    return text[:max_length].rsplit(' ', 1)[0] + "..."
