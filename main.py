from fastapi import FastAPI, HTTPException
import httpx
from typing import Dict, Any

app = FastAPI(title="JSONPlaceholder API Consumer", version="1.0.0")

# JSONPlaceholder API base URL
JSONPLACEHOLDER_BASE_URL = "https://jsonplaceholder.typicode.com"


@app.get("/")
async def root() -> Dict[str, str]:
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the JSONPlaceholder API Consumer!"}


@app.get("/posts/{id}")
async def get_post(id: int) -> Dict[str, Any]:
    """
    Get a post by ID from JSONPlaceholder API.
    
    Args:
        id: The post ID to retrieve
        
    Returns:
        The post data as JSON
        
    Raises:
        HTTPException: 404 if post not found
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{JSONPLACEHOLDER_BASE_URL}/posts/{id}")
            
            # Check if post exists
            if response.status_code == 404:
                raise HTTPException(status_code=404, detail="Post not found")
            
            # Raise for other HTTP errors
            response.raise_for_status()
            
            return response.json()
            
        except httpx.HTTPError as e:
            # Handle network errors
            raise HTTPException(status_code=500, detail=f"Error fetching post: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)