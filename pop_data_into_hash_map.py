# Problem:
# You are given a list of orders. Each order is a tuple of (customer_id, amount_spent).
# Your task is to aggregate the total amount spent by each customer and store the results in a hashmap (dictionary).

orders = [(101, 50), (102, 75), (101, 25), (103, 100), (102, 50)]

# Expected Output:
# {
#     101: 75,   # Customer 101 spent 50 + 25 = 75
#     102: 125,  # Customer 102 spent 75 + 50 = 125
#     103: 100   # Customer 103 spent 100
# }

def aggregate_customer_spending(orders):
    spending_map = {}  # Initialize an empty dictionary (hashmap)

    for customer_id, amount in orders:  # Iterate through each (customer_id, amount) pair
        if customer_id in spending_map:
            spending_map[customer_id] += amount  # Update existing customer’s total spending
        else:
            spending_map[customer_id] = amount  # First entry for the customer

    return spending_map  # Return the aggregated spending per customer

# Example Run
orders = [(101, 50), (102, 75), (101, 25), (103, 100), (102, 50)]
result = aggregate_customer_spending(orders)
print(result)


