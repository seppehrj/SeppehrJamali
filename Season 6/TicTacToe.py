import pyfiglet
import time
import random
from colorama import Fore, Style

def exitt():
    print("have a good lock")
    exit()

def show():
    for row in game_board:
        for cell in row:
            if cell == "X":
                print(Fore.RED + cell, end=" ")
            elif cell == "O":
                print(Fore.BLUE + cell, end=" ")
            else:
                print(cell, end=" ")
        print(Style.RESET_ALL)

def checkpoint():
    if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
        print("Player 1 win")
        end_time = time.time()
        print("Elapsed time: ", int(end_time - start) , "Second")
        return exitt()
                
    elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
        print("Player 1 win")
        end_time = time.time()
        print("Elapsed time: ", int(end_time - start) , "Second")
        return exitt()

    elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
        print("Player 1 win")
        end_time = time.time()
        print("Elapsed time: ", int(end_time - start) , "Second")
        return exitt()

    elif game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O":
        print("Player 2 win")
        end_time = time.time()
        print("Elapsed time: ", int(end_time - start) , "Second")
        return exitt()
        
    elif game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O":
        print("Player 2 win")
        end_time = time.time()
        print("Elapsed time: ", int(end_time - start) , "Second")
        return exitt()

    elif game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O":
        print("Player 2 win")
        end_time = time.time()
        print("Elapsed time: ", int(end_time - start) , "Second")
        return exitt()
                
    elif game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
        print("Player 1 win")
        end_time = time.time()
        print("Elapsed time: ", int(end_time - start) , "Second")
        return exitt()

    elif game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
        print("Player 1 win")
        end_time = time.time()
        print("Elapsed time: ", int(end_time - start) , "Second")
        return exitt()
        
    elif game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
        print("Player 1 win")
        end_time = time.time()
        print("Elapsed time: ", int(end_time - start) , "Second")
        return exitt()

    elif game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X": 
        print("Player 1 win")
        end_time = time.time()
        print("Elapsed time: ", int(end_time - start) , "Second")
        return exitt()

    elif game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O":
        print("Player 2 win")
        end_time = time.time()
        print("Elapsed time: ", int(end_time - start) , "Second")
        return exitt()

    elif game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O":
        print("Player 2 win")
        end_time = time.time()
        print("Elapsed time: ", int(end_time - start) , "Second")
        return exitt()

    elif game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O":
        print("Player 2 win")
        end_time = time.time()
        print("Elapsed time: ", int(end_time - start) , "Second")
        return exitt()
    
    elif game_board[0][0] == "0" and game_board[1][1] == "0" and game_board[2][2] == "0": 
        print("Player 2 win")
        end_time = time.time()
        print("Elapsed time: ", int(end_time - start) , "Second")
        return exitt()
       

    elif rounds == 9:
        print("Tasavi")
        end_time = time.time()
        print("Elapsed time: ", int(end_time - start) , "Second")

        return exitt()
           
title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)
print("Player vs Player its 0 & Player vs CPU its 1")
n = str(input("PvP or PvC / 0 or 1: "))

rounds = 0
second = 0
start = time.time()
s = (start % 3600) % 60
game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]
show()
if n == "0":
    while True:                     
        print("Player 1")
        while True:      
            row = int(input("row: "))
            col = int(input("col: "))
            if 0 <= row <=2 and 0 <= col <=2:
                if game_board[row][col] == "-":
                    game_board[row][col] = "X"
                    rounds += 1
                    break
                else:
                    print("dont cheating!!")
            else:
                print("Choose 0 or 1 or 2")
        checkpoint()
        show()

        print("Player 2")
        while True:
            
            row = int(input("row: "))
            col = int(input("col: "))
            if 0 <= row <=2 and 0 <= col <=2:
                if game_board[row][col] == "-":
                    game_board[row][col] = "O"
                    rounds += 1
                    break
                else:
                    print("dont cheating!!")
            else:
                print("Choose 0 or 1 or 2")
        checkpoint()
        show()

if n == "1":
    while True:                    
        print("Player 1")
        while True:
            
            row = int(input("row: "))
            col = int(input("col: "))
            if 0 <= row <=2 and 0 <= col <=2:
                if game_board[row][col] == "-":
                    game_board[row][col] = "X"
                    rounds += 1
                    break
                else:
                    print("dont cheating!!")
            else:
                print("Choose 0 or 1 or 2")
        checkpoint()
        show()

        print("Player 2")
        while True:       
            row = random.randint(0,2)
            col = random.randint(0,2)

            if game_board[row][col] == "-":
                game_board[row][col] = "O"
                rounds += 1
                break
        checkpoint()
        show()
