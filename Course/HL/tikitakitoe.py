# idk i wrote this on notepad 
import sys

WINS = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Cols
    (0, 4, 8), (2, 4, 6)              # Diagonals
)

def print_board(board):
    print(f"\n   A   B   C\n1  {board[0]} | {board[1]} | {board[2]}")
    print(f"  ---+---+---\n2  {board[3]} | {board[4]} | {board[5]}")
    print(f"  ---+---+---\n3  {board[6]} | {board[7]} | {board[8]}\n")

def get_index(text):
    text = text.upper()
    col = next((c for c in text if c in 'ABC'), None)
    row = next((c for c in text if c in '123'), None)

    if col and row:
        return ('ABC'.index(col)) + (int(row) - 1) * 3
    return None

def check_win(board, player):
    return any(all(board[i] == player for i in line) for line in WINS)

def main():
    board = [' '] * 9
    turn = 'X'
    moves = 0

    print("Enter moves like uhhh 'OB2'")

    while True:
        print_board(board)
        user_input = input(f"Player {turn} move: ")
        
        # Check for quit
        if user_input.lower() in ('q', 'quit', 'exit'):
            break

        idx = get_index(user_input)

        # Validation
        if idx is None:
            print("Do something like OB1 or something man")
            continue
        if board[idx] != ' ':
            print("square taken bozo")
            continue

        # Execute Move
        board[idx] = turn
        moves += 1

        # Check Win
        if check_win(board, turn):
            print_board(board)
            print(f"Checkimato Player {turn} wins!")
            break

        # Check Draw
        if moves == 9:
            print_board(board)
            print("Stalemate, what an skill issue")
            break

        # Switch Player
        turn = 'O' if turn == 'X' else 'X'

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nRage quit")
