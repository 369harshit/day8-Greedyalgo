class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(items, capacity):
    # Sort the items based on their value-to-weight ratio in descending order
    sorted_items = sorted(items, key=lambda item: item.ratio, reverse=True)

    total_value = 0
    total_weight = 0


    for item in sorted_items:
        if total_weight + item.weight <= capacity:
            # Add the whole item
            total_value += item.value
            total_weight += item.weight
            
        else:
            # Add a fraction of the item
            fraction = (capacity - total_weight) / item.weight
            partial_value = item.value * fraction
            total_value += partial_value
            break
    return total_value


# Example usage
items = [
    Item(60, 10),
    Item(100, 20),
    Item(120, 30)
]

knapsack_capacity = 50
total_value = fractional_knapsack(items, knapsack_capacity)

# Print the output
print("Maximum value is:", total_value)
