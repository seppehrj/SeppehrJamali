n = int(input("How many Fibonacci numbers would you like to see?"))
a = 1
b = 1
numbers = 0
if n <= 0:
    print("The number is wrong")
if n == 1:
    print(a, b)
else:
    print("Fiboo: ")
    while numbers < n:
        print(a)
        c = a + b
        a = b
        b = c
        numbers = numbers + 1
