from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

STUDENT_N = 1
app = FastAPI(title=f"Order Service N{STUDENT_N}")

# Внутрішня адреса сервісу в мережі Docker
INVENTORY_URL = "http://inventory-service:8000"
ORDERS = []


class OrderRequest(BaseModel):
    item_id: int
    quantity: int


@app.post("/orders")
def create_order(order: OrderRequest):
    """Створення замовлення з перевіркою наявності"""
    try:
        # Синхронний запит до Inventory Service
        response = requests.get(f"{INVENTORY_URL}/stock/{order.item_id}")
    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=503,
                            detail="Inventory Service is unavailable")

    if response.status_code == 404:
        raise HTTPException(status_code=400,
                            detail="Item does not exist")

    stock_data = response.json()["data"]

    # Перевірка наявності на складі
    if stock_data["quantity"] < order.quantity:
        raise HTTPException(status_code=400,
                            detail="Not enough stock")

    new_order = {
        "order_id": STUDENT_N * 100 + len(ORDERS) + 1,
        "item_id": order.item_id,
        "quantity": order.quantity,
        "status": "Created",
    }
    ORDERS.append(new_order)
    return {"student_id": STUDENT_N, "data": new_order}


@app.get("/orders")
def get_orders():
    """Список усіх замовлень"""
    return {"student_id": STUDENT_N, "data": ORDERS}