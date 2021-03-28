
# Функция фибоначи которая принимает одно значение
def fib(number):
# создание переменных и их вывод
    first_number = 1
    second_number = 1
    i = 2
    if number == 1:
        print(first_number)
    if number == 2:
        print(first_number)
        print(second_number)
    if number > i:
        print(first_number)
        print(second_number)
    # Пока i меньше значения
        while i < number:
    # Увеличиваем на 1
            i += 1
    # Новой переменной присваеваем сумму и вывоводим
            third_number = first_number + second_number
            print(third_number)
    # Присваеваем значения чтобы продолжить последовательность
            first_number = second_number
            second_number = third_number


# Заполняем функцию значением
fib(7)



# Рекурсивная функция фибоначи 
def fib(number):
# Если значение равно или меньше 1 то возврат равен 1
    if number <= 1: return 1
# Во всех остальных случаях возвращается данное арифметическое выражение
    else: return fib(number - 1) + fib(number - 2)

print(fib(6))



# Итеративный вывод
for i in range(7):
    print(fib(i))
