
def split(numbers):
    mid = len(numbers) // 2
    left = []
    for i in range(mid):
        left.append(numbers[i])
    right = []
    for i in range(mid, len(numbers)):
        right.append(numbers[i])
    return left, right


def merge(left, right, numbers):
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            numbers[left_idx + right_idx] = left[left_idx]
            left_idx += 1
        else:
            numbers[left_idx + right_idx] = right[right_idx]
            right_idx += 1
    for left_idx in range(left_idx, len(left)):
        numbers[left_idx + right_idx] = left[left_idx]
    for right_idx in range(right_idx, len(right)):
        numbers[left_idx + right_idx] = right[right_idx]
    return numbers


def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    left, right = split(numbers)
    return merge(merge_sort(left), merge_sort(right), numbers)


numbers = [6, 5, 3, 1, 8, 0, 7, 2, 4]
print(merge_sort(numbers))
assert merge_sort(numbers) == [8, 7, 6, 5, 4, 3, 2, 1, 0]
assert merge([8, 7, 6, 5, 4], [3, 2, 1, 0], numbers) == [8, 7, 6, 5, 4, 3, 2, 1, 0]
assert split(numbers) == ([8, 7, 6, 5], [4, 3, 2, 1, 0])

