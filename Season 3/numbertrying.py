import random

n = int(input("Enter your number: "))
user_num = []
new_list = []
for i in range(n):
    x = random.randint(0,n)
    user_num.append(x)
for x in user_num:
    if x not in new_list:
        new_list.append(x)

print(new_list)