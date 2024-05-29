def print_order_details(orders):
    for order in orders:
        customer_name, product, quantity = order
        print(f"Customer: {customer_name}, Product: {product}, Quantity: {quantity}")

# Sample Order Data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

# Call the function to print the order details
print_order_details(orders)
