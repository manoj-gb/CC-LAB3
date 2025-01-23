from products import dao

class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data):
        # Avoid dictionary lookups more than once
        return Product(data["id"], data["name"], data["description"], data["cost"], data.get("qty", 0))


def list_products():
    # Inline list comprehension for less overhead
    return [Product(product["id"], product["name"], product["description"], product["cost"], product.get("qty", 0)) 
            for product in dao.list_products()]


def get_product(product_id: int):
    # Direct loading without creating intermediate variables
    data = dao.get_product(product_id)
    return Product(data["id"], data["name"], data["description"], data["cost"], data.get("qty", 0))


def add_product(product: dict):
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    # Skip unnecessary checks unless critical
    dao.update_qty(product_id, qty)

