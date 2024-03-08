


n = int(input("enter your number: "))
if n < 0:
    print("sorry, factorial does not exist for negative numbers")
else:
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
        if factorial == n:
            print("Yes")
            break
        elif factorial > n:
            print("No")
            break
print
