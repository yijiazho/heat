from fastapi import FastAPI

app = FastAPI()

# Define a simple route
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

# Define a dynamic route
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
