class EndGame(Exception):
    pass


class BoardCellState:
    EMPTY = " "
    PLAYER_1 = "X"
    PLAYER_2 = "O"


def get_player_input(message):
    player_input = input(message)
    if player_input.lower() in ["quit", "exit", "stop", "leave", "end"]:
        raise EndGame()
    return player_input


def draw_game_board(board_state):
    board_render_template = """
+---+---+---+
| 0 | 1 | 2 |
+---+---+---+
| 3 | 4 | 5 |
+---+---+---+
| 6 | 7 | 8 |
+---+---+---+
"""


def run_game():
    board_state = [[BoardCellState.EMPTY for _ in range(3)] for _ in range(3)]
    try:
        while True:
            draw_game_board()
            get_player_move()
            check_victory_condition()
    except EndGame:
        print("GAME OVER")


if __name__ == "__main__":
    run_game()
