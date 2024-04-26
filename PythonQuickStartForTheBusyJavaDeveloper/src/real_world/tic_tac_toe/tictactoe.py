def initialize_board():
    board = [['-' for col in range(3)] for row in range(3)]
    return board


def print_board(board):
    print("-------------")

    for row in range(3):
        print("| ", end="")
        for col in range(3):
            print(board[row][col] + " | ", end="")
        print()
        print("-------------")


def place_mark(board, row, col, current_player_mark):
    if board[row][col] == '-':
        board[row][col] = current_player_mark
        return True

    return False


def check_for_win(board, current_player_mark):
    return check_rows_for_win(board, current_player_mark) or \
           check_columns_for_win(board, current_player_mark) or \
           check_diagonals_for_win(board, current_player_mark)


def check_all_same(c1, c2, c3, current_player_mark):
    return c1 == current_player_mark and c1 == c2 and c2 == c3


def check_rows_for_win(board, current_player_mark):
    for row in range(3):
        if check_all_same(board[row][0], board[row][1], board[row][2], current_player_mark):
            return True

    return False


def check_columns_for_win(board, current_player_mark):
    for col in range(3):
        if check_all_same(board[0][col], board[1][col], board[2][col], current_player_mark):
            return True

    return False


def check_diagonals_for_win(board, current_player_mark):
    return check_all_same(board[0][0], board[1][1], board[2][2],
                          current_player_mark) or \
           check_all_same(board[0][2], board[1][1], board[2][0],
                          current_player_mark)


def print_board_nicer(board):
    for row in range(3):
        for col in range(3):
            print(" " + str(board[row][col]) + " ", end="")
            if col < 2:
                print("|", end="")
        print()
        if row < 2:
            print("---+---+---")


def main():
    tictactoe_board = initialize_board()
    print_board(tictactoe_board)

    place_mark(tictactoe_board, 0, 0, 'X')
    place_mark(tictactoe_board, 1, 1, 'O')
    place_mark(tictactoe_board, 0, 1, 'X')

    print_board(tictactoe_board)

    place_mark(tictactoe_board, 2, 1, 'O')
    place_mark(tictactoe_board, 0, 2, 'X')

    print_board(tictactoe_board)
    print("Winner O?", check_for_win(tictactoe_board, 'O'))
    print("Winner X?", check_for_win(tictactoe_board, 'X'))

    print_board_nicer(tictactoe_board)

if __name__ == "__main__":
    main()
