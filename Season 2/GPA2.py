all_score = 0
number_scores = 0
while True:
    score = input("Enter your score: ")
    print("Use the command 'exit' to view the average and exit: ")
    if score == "exit":
        break

    all_score = float(score) + all_score
    number_scores = number_scores + 1  
      
resault = all_score / number_scores
print("moadel Shoma: ", resault)
        


