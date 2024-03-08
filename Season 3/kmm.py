a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b :
    c = a
else:
    c = b

while c % a != 0 or c % b != 0 :
    c += 1

print ("kmm", a , "and", b , "is",c)