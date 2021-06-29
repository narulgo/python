x = abs(int(input("Insert range of sequence: ")))
f1 = f2 = 1
print(f1,f2,end=" ")
for y in range(x-2):
    print(f1 + f2, end=" ")
    f1, f2 = f2, f1 + f2


x = abs(int(input("Choose the element to find its value: ")))
f1 = f2 =1
y = 2
while y < x:
    f1, f2 = f2, f1+f2
    y += 1
print("The value of the ",x," element is =", f2)


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


def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result

print(fibs(10))