#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    """Check if the board is full."""
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(prompt):
    """Prompt the user for valid input."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0 or value > 2:
                print("Please enter a number between 0 and 2.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get valid row and column inputs
        row = get_valid_input("Enter row (0, 1, or 2): ")
        col = get_valid_input("Enter column (0, 1, or 2): ")
        
        # Check if the spot is already taken
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue
        
        # Place the player's mark on the board
        board[row][col] = current_player
        
        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        # Check for a draw
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
