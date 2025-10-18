import unittest
from app.Order import Order


class OrderTestCase(unittest.TestCase):

    # ✅ Valid input tests
    def test_order_id_is_valid(self):
        # arrange
        order_id = "abc123"
        items = [{"order_item_id": "item1", "price": 10.0}, {"order_item_id": "item2", "price": 20.0}]
        # act
        order = Order(order_id, 456, 99.99, 789, items)
        # assert
        self.assertEqual(order.order_id(), order_id)

    def test_order_number_is_valid(self):
        # arrange
        order_number = 456
        items = [{"order_item_id": "item1", "price": 10.0}, {"order_item_id": "item2", "price": 20.0}]
        # act
        order = Order("abc123", order_number, 99.99, 789, items)
        # assert
        self.assertEqual(order.order_number(), order_number)
        self.assertEqual(order.order_number.format(), "ORDER-456")

    def test_order_number_format_is_valid(self):
        # arrange
        order_number = 456
        items = [{"order_item_id": "item1", "price": 10.0}, {"order_item_id": "item2", "price": 20.0}]
        # act
        order = Order("abc123", order_number, 99.99, 789, items)
        # assert
        self.assertEqual(order.order_number.format(), "ORDER-456")

    def test_amount_is_valid(self):
        # arrange
        amount = 99.99
        items = [{"order_item_id": "item1", "price": 10.0}, {"order_item_id": "item2", "price": 20.0}]
        # act
        order = Order("abc123", 456, amount, 789, items)
        # assert
        self.assertEqual(order.amount(), amount)

    def test_customer_id_is_valid(self):
        # arrange
        customer_id = 789
        items = [{"order_item_id": "item1", "price": 10.0}, {"order_item_id": "item2", "price": 20.0}]
        # act
        order = Order("abc123", 456, 99.99, customer_id, items)
        # assert
        self.assertEqual(order.customer_id(), customer_id)

    def test_order_items_count_is_correct(self):
        # arrange
        items = [
            {"order_item_id": "item1", "price": 10.0, "discount": 2.0},
            {"order_item_id": "item2", "price": 20.0}
        ]
        # act
        order = Order("abc123", 456, 99.99, 789, items)
        # assert
        self.assertEqual(order.order_items.count(), 2)

    def test_order_item_1_id_is_correct(self):
        # arrange
        items = [
            {"order_item_id": "item1", "price": 10.0, "discount": 2.0},
            {"order_item_id": "item2", "price": 20.0}
        ]
        # act
        order = Order("abc123", 456, 99.99, 789, items)
        # assert
        self.assertEqual(order.order_items()[0].order_item_id(), "item1")

    def test_order_item_1_price_is_correct(self):
        # arrange
        items = [{"order_item_id": "item1", "price": 10.0, "discount": 2.0}]
        # act
        order = Order("abc123", 456, 99.99, 789, items)
        # assert
        self.assertEqual(order.order_items()[0].price(), 10.0)

    def test_order_item_1_discount_is_correct(self):
        # arrange
        items = [{"order_item_id": "item1", "price": 10.0, "discount": 2.0}]
        # act
        order = Order("abc123", 456, 99.99, 789, items)
        # assert
        self.assertEqual(order.order_items()[0].discount(), 2.0)

    def test_order_item_1_total_price_is_correct(self):
        # arrange
        items = [{"order_item_id": "item1", "price": 10.0, "discount": 2.0}]
        # act
        order = Order("abc123", 456, 99.99, 789, items)
        # assert
        self.assertEqual(order.order_items()[0].total_price(), 8.0)

    def test_order_item_2_id_is_correct(self):
        # arrange
        items = [
            {"order_item_id": "item1", "price": 10.0, "discount": 2.0},
            {"order_item_id": "item2", "price": 20.0}
        ]
        # act
        order = Order("abc123", 456, 99.99, 789, items)
        # assert
        self.assertEqual(order.order_items()[1].order_item_id(), "item2")

    def test_order_item_2_price_is_correct(self):
        # arrange
        items = [{"order_item_id": "item2", "price": 20.0}]
        # act
        order = Order("abc123", 456, 99.99, 789, items)
        # assert
        self.assertEqual(order.order_items()[0].price(), 20.0)

    def test_order_item_2_discount_defaults_to_zero(self):
        # arrange
        items = [{"order_item_id": "item2", "price": 20.0}]
        # act
        order = Order("abc123", 456, 99.99, 789, items)
        # assert
        self.assertEqual(order.order_items()[0].discount(), 0.0)

    def test_order_item_2_total_price_is_correct(self):
        # arrange
        items = [{"order_item_id": "item2", "price": 20.0}]
        # act
        order = Order("abc123", 456, 99.99, 789, items)
        # assert
        self.assertEqual(order.order_items()[0].total_price(), 20.0)

    # ❌ Invalid input tests with error printing
    def test_invalid_order_id(self):
        with self.assertRaises(ValueError) as e:
            Order("", 456, 99.99, 789, ["item1", "item2"])
        print(e.exception)

        with self.assertRaises(ValueError) as e:
            Order(None, 456, 99.99, 789, ["item1", "item2"])
        print(e.exception)

        with self.assertRaises(ValueError) as e:
            Order(123, 456, 99.99, 789, ["item1", "item2"])
        print(e.exception)

    def test_invalid_order_number(self):
        with self.assertRaises(ValueError) as e:
            Order("abc123", 0, 99.99, 789, ["item1", "item2"])
        print(e.exception)

        with self.assertRaises(ValueError) as e:
            Order("abc123", -1, 99.99, 789, ["item1", "item2"])
        print(e.exception)

        with self.assertRaises(ValueError) as e:
            Order("abc123", "456", 99.99, 789, ["item1", "item2"])
        print(e.exception)

    def test_invalid_amount(self):
        with self.assertRaises(ValueError) as e:
            Order("abc123", 456, 0, 789, ["item1", "item2"])
        print(e.exception)

        with self.assertRaises(ValueError) as e:
            Order("abc123", 456, -10.5, 789, ["item1", "item2"])
        print(e.exception)

        with self.assertRaises(ValueError) as e:
            Order("abc123", 456, "99.99", 789, ["item1", "item2"])
        print(e.exception)

    def test_invalid_customer_id(self):
        with self.assertRaises(ValueError) as e:
            Order("abc123", 456, 99.99, 0, ["item1", "item2"])
        print(e.exception)

        with self.assertRaises(ValueError) as e:
            Order("abc123", 456, 99.99, -1, ["item1", "item2"])
        print(e.exception)

        with self.assertRaises(ValueError) as e:
            Order("abc123", 456, 99.99, "789", ["item1", "item2"])
        print(e.exception)

    def test_invalid_order_items(self):
        with self.assertRaises(ValueError) as e:
            Order("abc123", 456, 99.99, 789, "item1")
        print(e.exception)

        with self.assertRaises(ValueError) as e:
            Order("abc123", 456, 99.99, 789, [1, 2])
        print(e.exception)

        with self.assertRaises(ValueError) as e:
            Order("abc123", 456, 99.99, 789, [None, "item2"])
        print(e.exception)


if __name__ == '__main__':
    unittest.main()
