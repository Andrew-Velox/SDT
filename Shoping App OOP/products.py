
class Product(): # like menu
    def __init__(self):
        self.product_list = []

    def add_product(self, product):
        self.product_list.append(product)
        print(f"{product.name} has been added to the product list.")

    def show_products(self):
        if not self.product_list:
            print("No products available")
        else:
            print("\n\tAvailable Products:\n")
            for product in self.product_list:
                if product.quantity <= 0:
                    continue
                print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

    def find_product(self, name):
        for product in self.product_list:
            if product.name.lower() == name.lower():
                return product
        return None
    

