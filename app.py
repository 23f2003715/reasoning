import re
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Problem(BaseModel):
    problem_id: str
    problem: str

@app.post("/solve")
async def solve(p: Problem):
    text = p.problem

    # Extract numbers and percentages
    numbers = [int(n) for n in re.findall(r"\b\d+\b", text)]
    percents = [int(n) for n in re.findall(r"(\d+)%", text)]

    # Example: detect base cost, discount, tax
    # (You’ll need more robust parsing logic here)
    qty, price = numbers[0], numbers[1]
    base = qty * price
    discount = percents[0] if percents else 0
    tax = percents[1] if len(percents) > 1 else 0

    subtotal = base * (1 - discount/100)
    total = int(round(subtotal * (1 + tax/100)))

    reasoning = (
        f"Base = {qty} * {price} = {base}. "
        f"Apply {discount}% discount: {base} * {(100-discount)/100} = {subtotal}. "
        f"Add {tax}% tax: {subtotal} * {(100+tax)/100} = {total}. "
        f"Other numbers in the text are irrelevant."
    )

    return {"reasoning": reasoning, "answer": total}
