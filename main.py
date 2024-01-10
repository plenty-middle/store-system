# main.py

from product import Product
from customer import Customer
from online_store import OnlineStore

# Create products
product1 = Product(1, "Laptop", 800.0)
product2 = Product(2, "Smartphone", 400.0)

# Create customers
customer1 = Customer(101, "Alice", "alice@example.com")
customer2 = Customer(102, "Bob", "bob@example.com")

# Create an online store
online_store = OnlineStore()

# Add products and customers to the online store
online_store.add_product(product1)
online_store.add_product(product2)
online_store.add_customer(customer1)
online_store.add_customer(customer2)

# Display available products and customers
online_store.display_products()
online_store.display_customers()
