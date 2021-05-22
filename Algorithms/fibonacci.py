def fib(number):
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
    
        while i < number:
            i += 1
            third_number = first_number + second_number
            print(third_number)
            first_number = second_number
            second_number = third_number

fib(7)


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10


if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
