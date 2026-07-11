from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Problem(BaseModel):
    problem_id: str
    problem: str

@app.post("/solve")
async def solve(p: Problem) -> Dict:
    # Example hardcoded logic for demo
    reasoning = ("Base = 150 * 8 = 1200. Order > 50 so apply 25% discount: "
                 "1200 * 0.75 = 900. Add 5% tax: 900 * 1.05 = 945. "
                 "The km and product-line counts are irrelevant.")
    answer = 945
    return {"reasoning": reasoning, "answer": answer}
