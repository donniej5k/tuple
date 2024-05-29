def join_catalogs(*catalogs):
    combined_catalog = ()
    for catalog in catalogs:
        combined_catalog += catalog
    return combined_catalog

# Example Catalogs
catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))
catalog3 = (("Headphones", 200), ("Monitor", 300))

# Join the catalogs
combined_catalog = join_catalogs(catalog1, catalog2, catalog3)

# Display the combined catalog
for product, price in combined_catalog:
    print(f"Product: {product}, Price: ${price}")

# Example usage output
# Product: Laptop, Price: $1000
# Product: Camera, Price: $500
# Product: Smartphone, Price: $800
# Product: Tablet, Price: $450
# Product: Headphones, Price: $200
# Product: Monitor, Price: $300
