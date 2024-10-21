from fastapi                    import FastAPI, HTTPException
from pydantic                   import BaseModel
from fastapi.responses          import StreamingResponse
from fastapi.middleware.cors    import CORSMiddleware

import logging
import rag_system
import uvicorn

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = FastAPI()

# Allow credentials
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create query class with pydantic BaseModel
class QueryRequest(BaseModel):
    input_str: str

@app.get("/")
def root():
    return {'message': "Server is running"}

@app.post("/query/christmas")
async def query(request: QueryRequest):
    try:
        query_str = request.input_str
        return StreamingResponse(rag_system.run_query(query_str), media_type="text/event-stream")
    except Exception as e:
        raise HTTPException(status_code=500, details=str(e))

@app.post("/query/sustainability")
async def query(request: QueryRequest):
    try:
        query_str = request.input_str
        return StreamingResponse(rag_system.run_query(query_str, christmas=False), media_type="text/event-stream")
    except Exception as e:
        raise HTTPException(status_code=500, details=str(e))

@app.post("/query/compare")
async def query(request: QueryRequest):
    try:
        query_str = request.input_str
        return StreamingResponse(rag_system.run_query(query_str, compare=True), media_type="text/event-stream")
    except Exception as e:
        raise HTTPException(status_code=500, details=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)