def is_king_in_check_from_string(board_string):
    board = board_string.strip().split("\n")
    
    if len(board) != len(board[0]):
        print("Error")
        return
    
    board_size = len(board)
    king_position = None
    
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 'K':
                king_position = (i, j)
                break
    
    if king_position is None:
        print("Error")
        return
    
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] != '.' and board[i][j] != 'K':
                piece = board[i][j]
                if piece == 'P':
                    if i == king_position[0] + 1 and (j == king_position[1] + 1 or j == king_position[1] - 1):
                        print("Success")
                        return
                elif piece == 'R':
                    if i == king_position[0] or j == king_position[1]:
                        print("Success")
                        return
                elif piece == 'B':
                    if abs(i - king_position[0]) == abs(j - king_position[1]):
                        print("Success")
                        return
                elif piece == 'Q':
                    if i == king_position[0] or j == king_position[1] or abs(i - king_position[0]) == abs(j - king_position[1]):
                        print("Success")
                        return
    
    print("Fail")

#Example board :

board = """\
...K....
R.......
........
........
........
........
........
........\
"""


if __name__ == "__main__":
    is_king_in_check_from_string(board)