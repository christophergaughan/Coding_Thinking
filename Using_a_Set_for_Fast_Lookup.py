# USING NESTED FOR LOOPS IS ALMOST ALWAYS THE WRONG ANSWER- OR AT THE VERY LEAST A LAST RESORT
# Below we can avoid a nested list (O(n^2)) with one of time complexity: O(n + m)
#
# Converting orders to a set: O(m)
# Checking membership in a set: O(1) per lookup (instead of O(m) for a list)
# List comprehension iterates through customers: O(n)


def find_customers_without_orders(customers, orders):
    orders_set = set(orders)  # Convert list to set (O(m))
    return [customer for customer in customers if customer not in orders_set]  # O(n)

# Sample Data
customers = [101, 102, 103, 104, 105]
orders = [102, 105]

print(find_customers_without_orders(customers, orders))
