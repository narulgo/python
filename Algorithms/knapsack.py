from __future__ import print_function

def knapsack_matrix(items, limit):
    matrix = [[0] * (limit + 1) for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        _, weight, value = items[i - 1]
        for w in range(1, limit + 1):
            if weight > w:
                matrix[i][w] = matrix[i - 1][w]
            else:
                matrix[i][w] = max(matrix[i - 1][w],
                                   matrix[i - 1][w - weight] + value)
    return matrix

def knapsack_items(items, limit):
    matrix = knapsack_matrix(items, limit)
    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = matrix[j][w] != matrix[j - 1][w]
        if was_added:
            name, weight, _ = items[j - 1]
            result.append(name)
            w -= weight
    return result

def knapsack_value(items, limit):
    matrix = knapsack_matrix(items, limit)
    return matrix[len(items)][limit]

def knapsack_weight(items, limit):
    matrix = knapsack_matrix(items, limit)
    w = limit
    for j in range(len(items), 0, -1):
        was_added = matrix[j][w] != matrix[j - 1][w]
        if was_added:
            _, weight, _ = items[j - 1]
            w -= weight
    return limit - w

if __name__ in '__main__':
    ITEMS = [('apple', 10, 100), ('watch', 3, 400), ('phone', 5, 500), ('milk', 20, 300)]
    MAX_WEIGHT = 10
    print('knapsack items :', knapsack_items(ITEMS, MAX_WEIGHT))
    print('knapsack value :', knapsack_value(ITEMS, MAX_WEIGHT))
    print('knapsack weight:', knapsack_weight(ITEMS, MAX_WEIGHT))