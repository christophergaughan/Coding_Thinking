from collections import defaultdict

def aggregate_customer_spending(orders):
    # NOTE: When using `defaultdict()`, we must explicitly specify the default factory function
    # (in this case, int) because Python needs to know what default value to assign to a missing key.
    spending_map = defaultdict(int)  # Default value is 0 for new keys

    for customer_id, amount in orders:
        spending_map[customer_id] += amount  # Automatically initializes to 0 if key doesn't exist

    return dict(spending_map)  # Convert defaultdict to regular dict

# Example Run
orders = [(101, 50), (102, 75), (101, 25), (103, 100), (102, 50)]
result = aggregate_customer_spending(orders)
print(result)