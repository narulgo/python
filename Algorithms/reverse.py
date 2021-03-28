
def reverse_list(numbers):
    for i in range(len(numbers) // 2):          
        temp = numbers[i]
        numbers[i] = numbers[-i - 1]
        numbers[-i - 1] = temp
    return numbers

numbers = [1, 2, 3, 4, 5]
print(reverse_list(numbers))

