from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

STUDENT_N = 1
app = FastAPI(title=f"Inventory Service N{STUDENT_N}")

# База даних. Початкові ID починаються з 100 * N
STOCK = {
    STUDENT_N * 100 + 1: {"name": "Laptop", "quantity": 10},
    STUDENT_N * 100 + 2: {"name": "Mouse", "quantity": 50},
}


class StockUpdate(BaseModel):
    item_id: int
    quantity_change: int


@app.get("/stock/{id}")
def get_stock(id: int):
    """Перевірка кількості товару"""
    if id not in STOCK:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"student_id": STUDENT_N, "data": STOCK[id]}


@app.post("/stock/update")
def update_stock(update: StockUpdate):
    """Зміна залишків товару"""
    if update.item_id not in STOCK:
        raise HTTPException(status_code=404, detail="Item not found")
    STOCK[update.item_id]["quantity"] += update.quantity_change
    return {"student_id": STUDENT_N, "data": STOCK[update.item_id]}
