board = [' ' for _ in range(9)]

winning_combos = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def print_board():
    print()
    for i in range(3):
        print(f"{board[i*3]} | {board[i*3+1]} | {board[i*3+2]}")
        if i < 2:
            print("--+---+--")
    print()

def check_winner(player):
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def board_full():
    return ' ' not in board

def minimax(is_ai_turn):
    if check_winner('O'):
        return 1
    elif check_winner('X'):
        return -1
    elif board_full():
        return 0

    if is_ai_turn:
        best_score = -1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                if score > best_score:
                    best_score = score
        return best_score

    else:
        best_score = 1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                if score < best_score:
                    best_score = score
        return best_score

def ai_move():
    best_score = -1000
    best_move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

def play_game():
    print("Welcome to Tic Tac Toe! You are X, AI is O.")
    print_board()

    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != ' ':
            print("That spot is already taken. Try again.")
            continue
        board[move] = 'X'
        print_board()

        if check_winner('X'):
            print("You win!")
            break
        if board_full():
            print("It's a draw!")
            break

        print("AI is making a move...")
        ai_move()
        print_board()

        if check_winner('O'):
            print("AI wins!")
            break
        if board_full():
            print("It's a draw!")
            break

play_game()
