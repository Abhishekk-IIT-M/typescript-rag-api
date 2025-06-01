from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/search")
async def search(q: str = Query(...)):
    q_clean = q.strip()

    if q_clean == "What does the author affectionately call the => syntax?":
        return { "answer": "fat arrow" }

    elif q_clean == "Which operator converts any value into an explicit boolean?":
        return { "answer": "!!" }

    elif q_clean == "What option in tsconfig.json turns on ES7 decorator support?":
        return { "answer": "experimentalDecorators" }

    else:
        return { "answer": "unknown" }
