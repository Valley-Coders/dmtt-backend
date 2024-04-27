from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинт для получения заказов со статусом "pending"


@router.get("/orders/pending", response_model=List[Order])
def get_pending_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).filter(
        Order.order_status == OrderStatus.PENDING).all()
    return orders

# Эндпоинт для получения заказов со статусом "in progress"


@router.get("/orders/in-progress", response_model=List[Order])
def get_in_progress_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).filter(
        Order.order_status == OrderStatus.IN_PROGRESS).all()
    return orders

# Эндпоинт для получения заказов со статусом "rejected"


@router.get("/orders/rejected", response_model=List[Order])
def get_rejected_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).filter(
        Order.order_status == OrderStatus.REJECTED).all()
    return orders

# Эндпоинт для получения заказов со статусом "accepted"


@router.get("/orders/accepted", response_model=List[Order])
def get_accepted_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).filter(
        Order.order_status == OrderStatus.ACCEPTED).all()
    return orders
