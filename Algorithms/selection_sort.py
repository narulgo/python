
def max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max


def move(numbers, idx):
    return [numbers[idx]] + numbers[:idx] + numbers[idx + 1:]


def selection_sort(numbers):
    for i in range(len(numbers)):
        sorted_numbers = numbers[:i]
        unsorted_numbers = numbers[i:]
        max_number = max(unsorted_numbers)
        numbers = sorted_numbers + move(unsorted_numbers, unsorted_numbers.index(max_number))
    return numbers


numbers = [10, 15, 3, 6, 7, 1, 3, 9, 10]
print(selection_sort(numbers))
assert move(numbers, 8) == [10, 10, 15, 3, 6, 7, 1, 3, 9]


