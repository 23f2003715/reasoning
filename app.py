 import re

def solve_problem(text: str):
    # Find quantities and prices
    qty_match = re.search(r'orders (\d+)', text)
    price_match = re.search(r'at (\d+) dollars each', text)
    discount_match = re.search(r'(\d+)% bulk discount', text)
    tax_match = re.search(r'(\d+)% tax', text)

    qty = int(qty_match.group(1)) if qty_match else 0
    price = int(price_match.group(1)) if price_match else 0
    base = qty * price

    discount = int(discount_match.group(1)) if discount_match else 0
    subtotal = base * (1 - discount/100)

    tax = int(tax_match.group(1)) if tax_match else 0
    total = int(round(subtotal * (1 + tax/100)))

    reasoning = (
        f"Base = {qty} * {price} = {base}. "
        f"Apply {discount}% discount: {subtotal}. "
        f"Add {tax}% tax: {total}. "
        f"Other numbers in the text are irrelevant."
    )

    return {"reasoning": reasoning, "answer": total}

