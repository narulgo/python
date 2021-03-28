def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


a, b = swap(5, 6)
print(a)
