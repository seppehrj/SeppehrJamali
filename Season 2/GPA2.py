all_score = 0
number_scores = 0
while True:
    score = input("Nomre Khodra Vared konid: ")
    print("baraye moshahede moadel az dastor >>exit<< estfade konid")
    if score == "exit":
        break

    all_score = float(score) + all_score
    number_scores = number_scores + 1  
      
resault = all_score / number_scores
print("moadel Shoma: ", resault)
        


