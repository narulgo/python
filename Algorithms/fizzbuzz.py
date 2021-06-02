def fizzbuzz(n):
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 2 == 0:
            res3 = 'fizzbuzz'
            print(res3)
        elif i % 2 == 0:
            res1 = 'fizz'
            print(res1)
        elif i % 3 == 0:
            res2 = 'buzz'
            print(res2)
        else:
            print(i)
        i = i + 1
fizzbuzz(6)