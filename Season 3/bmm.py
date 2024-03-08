a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    c = a
else:
    c = b
    
while a % c != 0 or b % c != 0:
    c -= 1
print("bmm", a, "and", b, "is",c)