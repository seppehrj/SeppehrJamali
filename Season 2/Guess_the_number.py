import random

pc_number = random.randint(1, 100)
print("The number is between (1 to 100) and you have 15 chances to guess the numbers correctly")
print("Good Lock")
x = int()
while True:
    human_number = int(input("guess: "))
   

    if pc_number == human_number:
        x = x + 1
        print("Excellent, you have become a slave")
        print("✔")
        print("Number of guesses: ", x)
        break
        

    elif pc_number > human_number:
        x = x + 1
        print("The number is incorrect")
        print("Hint: The desired number is higher than your guess ⏫")
        print("❌")
    elif pc_number < human_number:
        x = x + 1
        print("The number is incorrect")
        print("Hint: The desired number is lower than your guess ⏬")
        print("❌")