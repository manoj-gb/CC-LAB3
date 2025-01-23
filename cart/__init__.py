import json
from typing import List
from products import Product, get_product
from cart import dao


class Cart:
    def __init__(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict) -> "Cart":
        # Use static method and safer dict unpacking
        contents = [get_product(product_id) for product_id in json.loads(data["contents"])]
        return Cart(
            id=data["id"], 
            username=data["username"], 
            contents=contents, 
            cost=data["cost"]
        )


def get_cart(username: str) -> List[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    products_in_cart = []
    for cart_detail in cart_details:
        # Safely deserialize JSON without eval
        product_ids = json.loads(cart_detail["contents"])
        products_in_cart.extend(get_product(product_id) for product_id in product_ids)

    return products_in_cart


def add_to_cart(username: str, product_id: int) -> None:
    """Add a product to the user's cart."""
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int) -> None:
    """Remove a product from the user's cart."""
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str) -> None:
    """Delete the user's entire cart."""
    dao.delete_cart(username)

