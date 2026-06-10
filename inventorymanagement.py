class Product:
    inventory = []

    def __init__(self, product_id, name,category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier
        Product.inventory.append(self)

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        product_id = cls.inventory[-1].product_id + 1 if len(cls.inventory) > 0 else 1
        new_product = cls(product_id, name, category, quantity, price,supplier)
        return "Product added successfully"
    
    @classmethod
    def update_product(cls, product_id, quantity = None, price = None, supplier = None):
        for p in cls.inventory:
            if p.product_id == product_id:
                if quantity is not None:
                    p.quantity = quantity
                if price is not None:
                    p.price = price
                if supplier is not None:
                    p.supplier = supplier
                return "Product information updated successfully"
        return "Product not found"
    @classmethod
    def delete_product(cls, product_id):
        for p in cls.inventory:
            if p.product_id == product_id:
                cls.inventory.remove(p)
                return "Product deleted successfully"
        return "Product not found"

class Order:

    def __init__(self, order_id, products, customer_info = None):
        self.order_id = order_id
        self.products = products
        self.customer_info = customer_info

    def place_order(self, product_id, quantity, customer_info = None):
        for product in Product.inventory:
            if product.product_id == product_id and product.quantity >= quantity:
                product.quantity -= quantity
                self.products.append((product_id, quantity))
                if customer_info:
                    self.customer_info = customer_info
                return f"Order placed successfully. Order ID: {self.order_id}"
        return f"Order could not be placed. Product not found or insufficient quantity"
