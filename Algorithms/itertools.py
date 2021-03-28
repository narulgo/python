
from itertools import zip_longest
array = [1, 2, 3, 4]
array2 = [1, 2, 3, 4, 5]


def add(array, array2):
    return [a + b for a, b in zip_longest(array, array2, fillvalue=0)]


print(add(array, array2))
