def parse_sudoku(board_data: str) -> list[list]:
    return [[int(digit) for digit in row] for row in board_data.splitlines()]


def row_is_valid(board, row: int) -> bool:
    return len(set(board[row])) == 9


def column_is_valid(board: list[list], column: int) -> bool:
    return len(set(board[row][column] for row in range(9))) == 9


def subsquare_is_valid(board: list[list], subsquare: int) -> bool:
    subsquare_row = (subsquare // 3) * 3
    subsquare_column = (subsquare % 3) * 3

    subsquare_set = set()
    
    for row in range(subsquare_row, subsquare_row + 3):
        for column in range(subsquare_column, subsquare_column + 3):
            subsquare_set.add(board[row][column])
            
    return len(subsquare_set) == 9


def board_is_valid(board: list[list]) -> bool:
    for row in range(9):
        if not row_is_valid(board, row):
            return False

    for column in range(9):
        if not column_is_valid(board, column):
            return False

    for subsquare in range(9):
        if not subsquare_is_valid(board, subsquare):
            return False

    return True


valid_sample_input = """295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672"""

invalid_sample_input = """195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671"""


def main(data):
    board = parse_sudoku(data)
    if board_is_valid(board):
        print("Yes")
    else:
        print("No")

main(valid_sample_input)
main(invalid_sample_input)