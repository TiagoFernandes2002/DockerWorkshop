def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        print(f"Jogador {current_player}, é a tua vez.")
        row = int(input("Escolhe a linha (0, 1 ou 2): "))
        col = int(input("Escolhe a coluna (0, 1 ou 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Essa posição já está ocupada. Tenta novamente.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Parabéns! O jogador {current_player} venceu!")
            break

        if is_full(board):
            print_board(board)
            print("Empate! O tabuleiro está cheio.")
            break

        current_player = 'O' if current_player == 'X' else 'X'




if __name__ == "__main__":
    main()
