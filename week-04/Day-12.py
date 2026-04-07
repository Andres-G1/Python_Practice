#Day-12 on python
''' Hi :), this is Day-12 in Python.
Congratulations for reaching Day-12.
In this day you are completing a project with classes and modules.
'''

# Project: product catalog with classes
# The goal is to create a simple application that shows a catalog
# and applies a discount when the price is greater than 100000.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discounted_price(self):
        if self.price > 100000:
            return self.price * 0.85
        return self.price

    def show(self):
        price_text = f"{self.price:.2f}"
        discount_text = f"{self.discounted_price():.2f}" if self.price > 100000 else "Not applicable"
        print(f"{self.name} - Price: {price_text} - Discounted price: {discount_text}")


class Catalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_catalog(self):
        print("--- Product Catalog ---")
        for product in self.products:
            product.show()
        print("-----------------------")


def run_app():
    catalog = Catalog()
    catalog.add_product(Product("Laptop", 150000))
    catalog.add_product(Product("Mouse", 25000))
    catalog.add_product(Product("Keyboard", 120000))

    while True:
        print("\nMenu:")
        print("1. Show catalog")
        print("2. Add product")
        print("0. Exit")
        option = input("Select an option: ")

        if option == "1":
            catalog.show_catalog()
        elif option == "2":
            name = input("Product name: ")
            price = float(input("Product price: "))
            catalog.add_product(Product(name, price))
        elif option == "0":
            print("Exiting. Thank you for using the catalog.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    run_app()
