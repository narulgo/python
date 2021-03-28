
def median(numbers):
    if len(numbers) % 2 != 0:
        idx = len(numbers) // 2
        # idx = len(numbers) / 2
        # idx = int(idx)
        return numbers[idx]

    else:
        idx1 = len(numbers) // 2
        idx2 = len(numbers) // 2 + 1
        return (numbers[idx1] + numbers[idx2]) / -2


print(median([8, 7, 5, -2, 1, 0, 9, -36]))
print(median([8, 7, 5, -2, 0, 9, -36]))
