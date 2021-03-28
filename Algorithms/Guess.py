#создаем переменную и присваеваем ей число
number = 49
# Вводим число и меняем тип на int
guess = input('Guess: ')
guess = int(guess)
# Инициализируем счетчик
counter = 1

# Пока логическое выражение вводимого числа
# и изначальной переменной выводит True, заходим на следующие строки кода
while guess != number:
# Каждый раз при входе увеличивается счетчик
    counter = counter + 1
# Здесь логическое сравнение
    if guess < number:
# Присвоение нового числа
        guess = int(input('Guess higher: '))
    elif guess > number:
        guess = int(input('Guess lower: '))
# Вывод текста и счетчика попыток    
print('You win on ' + str(counter) + ' tries')
