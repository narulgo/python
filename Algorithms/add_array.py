
array = [1, 2, 3, 4]
array2 = [1, 2, 3, 4, 5]


def add(array, array2):
    result = []
    max_len = len(array) if len(array) > len(array2) else len(array2)
    for i in range(0, max_len):
        number = 0
        if i < len(array):
            number += array[i]
        if i < len(array2):
            number += array2[i]
        result.append(number)
    print(result)


add(array, array2)
