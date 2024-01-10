# online_store.py

from product import Product
from customer import Customer

class OnlineStore:
    def __init__(self):
        self.products = []
        self.customers = []

    def add_product(self, product):
        self.products.append(product)

    def add_customer(self, customer):
        self.customers.append(customer)

    def display_products(self):
        print("Available Products:")
        for product in self.products:
            product.display()

    def display_customers(self):
        print("Customers:")
        for customer in self.customers:
            customer.display()
