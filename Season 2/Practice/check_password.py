import time

for i in range(3):
    password = input("Enter the password: ")
    if password == "6565":
        print("successful")
        print("Welcome")
        break
    else:
        print("Wrong password")
    
time.sleep(30)
