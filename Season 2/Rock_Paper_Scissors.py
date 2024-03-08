import random

human_score = 0
pc_score = 0
x = random.randint(1, 3)
while pc_score < 5 and human_score < 5:
    if x == 1:
     pc_choice = "Rock"
    elif x == 2:
     pc_choice = "Paper"
    elif x == 3:
        pc_choice = "Scissor"

    human_choice = input("Rock/Paper/Scissor: ")
    if human_choice == "Rock" or human_choice == "Paper" or human_choice == "Scissor":

        print("💻", pc_choice)
        print("☺", human_choice)

        if pc_choice == "Rock" and human_choice == "Paper":
            human_score = human_score + 1

        elif pc_choice == "Rock" and human_choice == "Scissor":
            pc_score = pc_score + 1
        
        elif pc_choice == "Rock" and human_choice == "Rock":
            print(">>equal<<")

        elif pc_choice == "Paper" and human_choice == "Scissor":
            human_score = human_score + 1
        
        elif pc_choice == "Paper" and human_choice == "Rock":
            human_score = human_score + 1

        elif pc_choice == "Paper" and human_choice == "Paper":
            print(">>equal<<")

        elif pc_choice == "Scissor" and human_choice == "Rock":
            human_score = human_score + 1

        elif pc_choice == "Scissor" and human_choice == "Paper":
            pc_score = pc_score + 1

        elif pc_choice == "Scissor" and human_choice == "Scissor":
            print(">>equal<<")
        print("My score : ", human_score)
        print("Bot score: ", pc_score)

    else:
        print(">>Rock/Paper/Scissor<< type in")
if pc_score == 5:
    print("You lose😑")
if human_score == 5:
    print("You won🥰")



