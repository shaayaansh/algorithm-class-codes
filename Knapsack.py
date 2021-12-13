def knapsack(capacity, weights, values, n):
    if n == 0:
        return 0
    if capacity == 0:
        return 0
    if weights[n-1] > capacity:
        return knapsack(capacity, weights, values, n-1)

    else:
        return max(values[n-1]+knapsack(capacity-weights[n-1], weights, values, n-1),
                   knapsack(capacity, weights, values, n-1))


values = input("Please enter the values array with space between the values : \n")
values = values.split(" ")
for i in range(len(values)):
    values[i] = int(values[i])
weights = input("Please enter the weights array with space between the values : \n")
weights = weights.split(" ")
for i in range(len(weights)):
    weights[i] = int(weights[i])
capacity = int(input("Please enter the capacity : \n"))
print(knapsack(capacity, weights, values, len(weights)))
