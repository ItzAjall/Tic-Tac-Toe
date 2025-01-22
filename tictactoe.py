import random

def printBoard():
    print(f"1:[{board[0][0]}] 2:[{board[0][1]}] 3:[{board[0][2]}]\n")
    print(f"4:[{board[1][0]}] 5:[{board[1][1]}] 6:[{board[1][2]}]\n")
    print(f"7:[{board[2][0]}] 8:[{board[2][1]}] 9:[{board[2][2]}]\n")

def Winner(winner):
    printBoard()
    print(f"{winner} won the game!")
    exit()

def Move(ch, ai=False):
    selectedChoice[ch] = 1
    prefix = "O" if ai else "X"
    match ch:
        case 1:
            board[0][0] = prefix
        case 2:
            board[0][1] = prefix
        case 3:
            board[0][2] = prefix
        case 4:
            board[1][0] = prefix
        case 5:
            board[1][1] = prefix
        case 6:
            board[1][2] = prefix
        case 7:
            board[2][0] = prefix
        case 8:
            board[2][1] = prefix
        case 9:
            board[2][2] = prefix

def aiMove():
    check = checkIfPlayerIsWinning()
    if check:
        row, col = check
        selectedChoice[row * 3 + col + 1] = 1
        board[row][col] = "O"
    else:
        random_choice = random.randint(1, 9)
        while selectedChoice[random_choice] != 0:
            random_choice = random.randint(1, 9)
        Move(random_choice, ai=True)

def checkIfPlayerIsWinning():
    for i in range(3):
        if board[i][0] == board[i][1] == "X" and board[i][2] == " ":
            return (i, 2)
        if board[i][0] == board[i][2] == "X" and board[i][1] == " ":
            return (i, 1)
        if board[i][1] == board[i][2] == "X" and board[i][0] == " ":
            return (i, 0)

        if board[0][i] == board[1][i] == "X" and board[2][i] == " ":
            return (2, i)
        if board[0][i] == board[2][i] == "X" and board[1][i] == " ":
            return (1, i)
        if board[1][i] == board[2][i] == "X" and board[0][i] == " ":
            return (0, i)

    if board[0][0] == board[1][1] == "X" and board[2][2] == " ":
        return (2, 2)
    if board[0][0] == board[2][2] == "X" and board[1][1] == " ":
        return (1, 1)
    if board[1][1] == board[2][2] == "X" and board[0][0] == " ":
        return (0, 0)

    if board[2][0] == board[1][1] == "X" and board[0][2] == " ":
        return (0, 2)
    if board[2][0] == board[0][2] == "X" and board[1][1] == " ":
        return (1, 1)
    if board[1][1] == board[0][2] == "X" and board[2][0] == " ":
        return (2, 0)

    return None

def checkWinner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            winner = "Player" if board[i][0] == "X" else "Computer"
            Winner(winner)
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            winner = "Player" if board[0][i] == "X" else "Computer"
            Winner(winner)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        winner = "Player" if board[0][0] == "X" else "Computer"
        Winner(winner)
    elif board[2][0] == board[1][1] == board[0][2] and board[1][1] != " ":
        winner = "Player" if board[1][1] == "X" else "Computer"
        Winner(winner)

def checkDraw():
    if all(value != 0 for value in selectedChoice.values()):
        printBoard()
        print("It's a draw!")
        exit()

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
selectedChoice = {
    1: 0, 2: 0, 3: 0,
    4: 0, 5: 0, 6: 0,
    7: 0, 8: 0, 9: 0
}

printBoard()
while True:
    try:
        choice = int(input("Please Select a Block (1-9): "))
        if 1 <= choice <= 9:
            if selectedChoice[choice] == 0:
                Move(choice)
                checkWinner()
                checkDraw()
                aiMove()
                checkWinner()
                checkDraw()
                printBoard()
            else:
                print("This block has already been chosen")
        else:
            print("Please select a valid block between 1 and 9.")
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 9.")