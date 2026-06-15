customer_ids = [101, 102, 103, 101, 104, 102, 105, 103]

# 1. Remove duplicates by casting to a set
unique_ids_set = set(customer_ids)

# 2. Convert to a sorted list
sorted_unique_ids = sorted(unique_ids_set)

print("Unique customer IDs in sorted order:", sorted_unique_ids)