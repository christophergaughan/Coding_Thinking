# If you are going to find membership in a list-> turn it into a set
# Why is this better?
# set(vip_customers) allows O(1) lookups instead of O(n).
# Using a set for result avoids duplicate checks (no if customer not in result).
# Overall complexity: O(n + m) ≈ O(n) (Much better than O(n²)).


def find_vip_customers(orders, vip_customers):
    vip_set = set(vip_customers)  # Convert list to set (O(m))
    result = set()  # Use a set to store unique VIPs

    for customer in orders:  # O(n)
        if customer in vip_set:  # O(1) average lookup
            result.add(customer)  # O(1) average insert

    return list(result)  # Convert back to list


# Example run
orders = [102, 203, 304, 102, 405, 102, 506, 607]
vip_customers = [102, 506, 999]
print(find_vip_customers(orders, vip_customers))  # Output: [102, 506]
