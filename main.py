# making tic tac toe game in python with automatic respones 

board={1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}

def display_board():
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("-+-+-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-+-+-")
    print(board[7]+"|"+board[8]+"|"+board[9])

display_board()

def check_win(player):
    if board[1]==player and board[2]==player and board[3]==player:
        return True
    elif board[4]==player and board[5]==player and board[6]==player:
        return True
    elif board[7]==player and board[8]==player and board[9]==player:
        return True
    elif board[1]==player and board[4]==player and board[7]==player:
        return True
    elif board[2]==player and board[5]==player and board[8]==player:
        return True
    elif board[3]==player and board[6]==player and board[9]==player:
        return True
    elif board[1]==player and board[5]==player and board[9]==player:
        return True
    elif board[3]==player and board[5]==player and board[7]==player:
        return True
    else:
        return False
    
def check_tie():
    if " " not in board.values():
        return True
    else:
        return False
    
def minimax(ismaximizing):
    if check_win("X"):
        return 1
    elif check_win("O"):
        return -1
    elif check_tie():
        return 0
    if ismaximizing:
        best_score=-1000
        for key in board.keys():
            if board[key]==" ":
                board[key]="X"
                score=minimax(False)
                board[key]=" "
                best_score=max(score,best_score)
        return best_score
    else:
        best_score=1000
        for key in board.keys():
            if board[key]==" ":
                board[key]="O"
                score=minimax(True)
                board[key]=" "
                best_score=min(score,best_score)
        return best_score
    
def computer_move():
    best_score=-1000
    best_move=0
    for key in board.keys():
        if board[key]==" ":
            board[key]="X"
            score=minimax(False)
            board[key]=" "
            if score>best_score:
                best_score=score
                best_move=key
    return best_move

player="X"
while True:
    if player=="X":
        position=computer_move()
    else:
        position=int(input(f"enter the position for {player}:"))
    if board[position]!=" ":
        print("position taken try again")
        continue
    board[position]=player
    display_board()
    if check_win(player):
        print(f"player {player} won")
        break
    elif check_tie():
        print("tie")
        break

    
    if player=="X":
        player="O"
    else:
        player="X"
