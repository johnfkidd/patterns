from app.OrderItem import create_order_items
from app.wrappers import CallableValueObject


def create_order_id(value: str):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Order ID must be a non-empty string")
    return CallableValueObject(value)


def create_order_number(value: int):
    if not isinstance(value, int) or value <= 0:
        raise ValueError("Order Number must be a positive integer")
    return CallableValueObject(value, format=lambda: f"ORDER-{value}")


def create_amount(value: float):
    if not isinstance(value, float) or value <= 0:
        raise ValueError("Amount must be a positive number")
    return CallableValueObject(value)


def create_customer_id(value: int):
    if not isinstance(value, int) or value <= 0:
        raise ValueError("Customer ID must be a positive integer")
    return CallableValueObject(value)


class Order:
    def __init__(self, order_id, order_number, amount, customer_id, order_items: list[dict]):
        self.order_id = create_order_id(order_id)
        self.order_number = create_order_number(order_number)
        self.amount = create_amount(amount)
        self.customer_id = create_customer_id(customer_id)
        self.order_items = create_order_items(order_items)
