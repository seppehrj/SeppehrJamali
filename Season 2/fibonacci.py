n = int(input("Dost dari ta ch adadi fibo ro bbini"))
a = 1
b = 1
numbers = 0
if n <= 0:
    print("adad eshtebast")
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
