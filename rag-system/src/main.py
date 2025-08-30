from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional
import pandas as pd
import os
import random

app = FastAPI(
    title="RAG System",
    description="Retrieval-Augmented Generation system for document search",
    version="0.1.0"
)

EMBEDDING_DIM = 1536

class SearchResult(BaseModel):
    id: int
    title: str
    content: str
    category: str
    similarity_score: float
    embedding_summary: str

class SearchResponse(BaseModel):
    query: str
    results: List[SearchResult]
    total_results: int
    embedding_dimension: int

def load_synthetic_data():
    csv_path = os.path.join(os.path.dirname(__file__), "../db/synthetic/sample_docs.csv")
    try:
        df = pd.read_csv(csv_path)
        return df.to_dict('records')
    except FileNotFoundError:
        return []

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "rag-system", "embedding_dim": EMBEDDING_DIM}

@app.get("/search", response_model=SearchResponse)
async def search_documents(
    q: str = Query(..., description="Search query"),
    limit: int = Query(5, description="Maximum number of results"),
    category: Optional[str] = Query(None, description="Filter by category")
):
    documents = load_synthetic_data()
    
    if not documents:
        return SearchResponse(
            query=q,
            results=[],
            total_results=0,
            embedding_dimension=EMBEDDING_DIM
        )
    
    # Simple keyword matching simulation
    query_lower = q.lower()
    matches = []
    
    for doc in documents:
        score = 0.0
        title_lower = doc['title'].lower()
        content_lower = doc['content'].lower()
        
        # Calculate simple relevance score
        if query_lower in title_lower:
            score += 0.8
        if query_lower in content_lower:
            score += 0.6
        if query_lower in doc['embedding_summary'].lower():
            score += 0.4
            
        # Add some randomness to simulate embedding similarity
        score += random.uniform(0.1, 0.3)
        
        if score > 0.1:  # Threshold for relevance
            matches.append({
                'doc': doc,
                'score': min(score, 1.0)  # Cap at 1.0
            })
    
    # Sort by score and apply filters
    matches.sort(key=lambda x: x['score'], reverse=True)
    
    if category:
        matches = [m for m in matches if m['doc']['category'].lower() == category.lower()]
    
    # Limit results
    matches = matches[:limit]
    
    results = []
    for match in matches:
        doc = match['doc']
        results.append(SearchResult(
            id=doc['id'],
            title=doc['title'],
            content=doc['content'],
            category=doc['category'],
            similarity_score=match['score'],
            embedding_summary=doc['embedding_summary']
        ))
    
    return SearchResponse(
        query=q,
        results=results,
        total_results=len(results),
        embedding_dimension=EMBEDDING_DIM
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)