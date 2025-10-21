import os
import time

board = [' '] * 10  # index 1-9 used
player = 1
Win = 1
Draw = -1
Running = 0
Game = Running

def DrawBoard():
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("---|---|---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---|---|---")
    print(f" {board[7]} | {board[8]} | {board[9]} ")

def CheckPosition(x):
    return board[x] == ' '

def CheckWin():
    global Game
    win_pos = [
        (1,2,3), (4,5,6), (7,8,9),
        (1,4,7), (2,5,8), (3,6,9),
        (1,5,9), (3,5,7)
    ]
    for pos in win_pos:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != ' ':
            Game = Win
            return
    if ' ' not in board[1:]:
        Game = Draw
    else:
        Game = Running

print("-------- Welcome to TIC TAC TOE Game --------\n")
a = input("Enter name of player 1 -> ")
b = input("Enter name of player 2 -> ")
print("\nPlease Wait...")
time.sleep(2)

while Game == Running:
    os.system('cls' if os.name == 'nt' else 'clear')
    DrawBoard()
    
    current_player = a if player % 2 != 0 else b
    Mark = 'X' if player % 2 != 0 else 'O'
    
    print(f"{current_player}'s turn ({Mark})")
    
    while True:
        try:
            choice = int(input("Enter position [1-9]: "))
            if choice < 1 or choice > 9:
                print("Invalid input. Choose 1-9.")
            elif not CheckPosition(choice):
                print("Position already taken. Choose another.")
            else:
                break
        except ValueError:
            print("Invalid input. Enter a number.")

    board[choice] = Mark
    player += 1
    CheckWin()

os.system('cls' if os.name == 'nt' else 'clear')
DrawBoard()
if Game == Draw:
    print("Game Draw!")
else:
    winner = a if (player - 1) % 2 != 0 else b
    print(f"Congratulations! {winner} won the game!")
