from app.wrappers import CallableValueObject


def create_order_item_id(value: str):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Order Item ID must be a non-empty string")
    return CallableValueObject(value)


def create_price(value: float):
    if not isinstance(value, float) or value <= 0:
        raise ValueError("Price must be a positive number")
    return CallableValueObject(value)


def create_discount(value: float = 0.0):
    if not isinstance(value, float) or value < 0:
        raise ValueError("Discount must be a non-negative number")
    return CallableValueObject(value)


def create_order_items(items: list):
    if not isinstance(items, list):
        raise ValueError("Order items must be provided as a list")

    order_items = []
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("Each order item must be a dictionary")

        try:
            order_item = OrderItem(
                order_item_id=item["order_item_id"],
                price=item["price"],
                discount=item.get("discount", 0.0)
            )
            order_items.append(order_item)
        except KeyError as e:
            raise ValueError(f"Missing required field in order item: {e}")
        except ValueError as e:
            raise ValueError(f"Invalid order item: {e}")

    return CallableValueObject(order_items, count=lambda: len(order_items))


class OrderItem:
    def __init__(self, order_item_id: str, price: float, discount: float = 0.0):
        self.order_item_id = create_order_item_id(order_item_id)
        self.price = create_price(price)
        self.discount = create_discount(discount)

    def total_price(self):
        return self.price() - self.discount()
