n = int(input("enter your snake number: "))
number_n = 0
snake = str()
while number_n < n:
    snake+=("*")
    number_n +=1
    while number_n < n:
        snake+=("#")
        number_n +=1
        break
print(snake)
