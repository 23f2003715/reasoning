import re

def solve_problem(text: str):
    qty = 0
    price = 0
    discount = 0
    tax = 0

    qty_match = re.search(r'orders (\d+)', text)
    if qty_match:
        qty = int(qty_match.group(1))

    price_match = re.search(r'at (\d+) dollars each', text)
    if price_match:
        price = int(price_match.group(1))

    discount_match = re.search(r'(\d+)% bulk discount', text)
    if discount_match:
        discount = int(discount_match.group(1))

    tax_match = re.search(r'(\d+)% tax', text)
    if tax_match:
        tax = int(tax_match.group(1))

    base = qty * price
    subtotal = base * (1 - discount/100)
    total = int(round(subtotal * (1 + tax/100)))

    reasoning = (
        f"Base = {qty} * {price} = {base}. "
        f"Apply {discount}% discount: {subtotal}. "
        f"Add {tax}% tax: {total}. "
        f"Other numbers in the text are irrelevant."
    )

    return {"reasoning": reasoning, "answer": total}
