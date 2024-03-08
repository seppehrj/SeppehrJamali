import random

human_score = 0
pc_score = 0
x = random.randint(1, 3)
while pc_score < 5 and human_score < 5:
    if x == 1:
     pc_choice = "sang"
    elif x == 2:
     pc_choice = "kaqaz"
    elif x == 3:
        pc_choice = "qeychi"

    human_choice = input("sang/kaqaz/qeychi: ")
    if human_choice == "sang" or human_choice == "kaqaz" or human_choice == "qeychi":

        print("💻", pc_choice)
        print("☺", human_choice)

        if pc_choice == "sang" and human_choice == "kaqaz":
            human_score = human_score + 1

        elif pc_choice == "sang" and human_choice == "qeychi":
            pc_score = pc_score + 1
        
        elif pc_choice == "sang" and human_choice == "sang":
            print(">>Tasavi<<")

        elif pc_choice == "kaqaz" and human_choice == "qeychi":
            human_score = human_score + 1
        
        elif pc_choice == "kaqaz" and human_choice == "sang":
            human_score = human_score + 1

        elif pc_choice == "kaqaz" and human_choice == "kaqaz":
            print(">>Tasavi<<")

        elif pc_choice == "qeychi" and human_choice == "sang":
            human_score = human_score + 1

        elif pc_choice == "qeychi" and human_choice == "kaqaz":
            pc_score = pc_score + 1

        elif pc_choice == "qeychi" and human_choice == "qeychi":
            print(">>Tasavi<<")
        print("Score Man: ", human_score)
        print("Score bot: ", pc_score)

    else:
        print(">>sang/kaqaz/qeychi<< Ra Type konid")
if pc_score == 5:
    print("Shoma Bakhtid😑")
if human_score == 5:
    print("Shoma Barande Shodid🥰")



