import itertools
import random
import tkinter as tk
import warnings
from copy import deepcopy
from tkinter.font import Font
from tkinter.messagebox import showinfo, showwarning, askyesno
from typing import Literal, Callable, Any


class CellAlreadyClaimed(Exception):
    def __init__(self, by_player_id: int):
        super().__init__()
        self.by_player_id = by_player_id

    def __str__(self):
        return f"You cannot claim this cell. It is owned by player {self.by_player_id}."


class NotYourTurn(Exception):
    def __init__(self, player_of_this_turn: int):
        super().__init__()
        self.player_of_this_turn = player_of_this_turn

    def __str__(self):
        return f"You may not act because it is not your turn. It is player {self.player_of_this_turn}'s turn."


class GameOver(Exception):
    def __init__(self, winner_id: int):
        super().__init__()
        self.winner_id = winner_id

    def __str__(self):
        return f"You may not act because the game is over. It was won by player {self.winner_id}."


class TicTacToeGameLogic:
    class EventTypes:
        CELL_CLAIMED = 'cell_claimed'
        NEXT_TURN = 'next_turn'
        GAME_OVER = 'win_condition_met'

    def __init__(self, starts_on_player: Literal[1, 2] = 2):
        self._cells = {(row, column): 0 for row, column in itertools.product(range(3), range(3))}

        self.turn_iterator = itertools.cycle((1, 2))
        if starts_on_player == 2:
            next(self.turn_iterator)

        self._player_of_this_turn = starts_on_player
        self._game_is_over = False
        self._winner_id = None
        self.event_listeners = {}

    @property
    def cells(self):
        return deepcopy(self._cells)

    @property
    def player_of_this_turn(self) -> int:
        return self._player_of_this_turn

    @property
    def unclaimed_cells(self):
        return [position for position, owner_id in self._cells.items() if owner_id == 0]

    def get_cell_owner_id(self, row: int, column: int) -> int:
        return self._cells[row, column]

    def claim_cell(self, player_id: int, row: int, column: int):
        if self._winner_id:
            raise GameOver(winner_id=self._winner_id)

        if player_id != self.player_of_this_turn:
            raise NotYourTurn(player_of_this_turn=self.player_of_this_turn)

        if (cell_owner := self.get_cell_owner_id(row, column)) != 0:
            raise CellAlreadyClaimed(by_player_id=cell_owner)

        self._cells[row, column] = player_id
        self.dispatch_event(
            self.EventTypes.CELL_CLAIMED,
            data={'row': row, 'column': column, 'player_id': player_id}
        )

        self.check_if_game_is_over(player_id, row, column)

        if not self._game_is_over:
            self.transition_to_next_turn()

    def transition_to_next_turn(self):
        self._player_of_this_turn = next(self.turn_iterator)
        self.dispatch_event(self.EventTypes.NEXT_TURN, {'player_id': self._player_of_this_turn})

    def check_if_game_is_over(self, player_id: int, row: int, column: int) -> bool:
        lines_to_check = self.get_lines_that_include_target_cell(row, column)

        for line in lines_to_check:
            for cell_position in line:
                cell_owner_id = self._cells[cell_position]
                if player_id != cell_owner_id:
                    break
            else:
                # Execution will only reach this point if the given player owns every cell on the current line.
                self._game_is_over = True
                self._winner_id = player_id
                self.dispatch_event(self.EventTypes.GAME_OVER, {'winner_id': player_id})
                return True

        # If every space on the board is claimed and neither player has claimed a straight line,
        # the game ends in a draw.
        if len(self.unclaimed_cells) == 0:
            self._game_is_over = True
            self._winner_id = 0
            self.dispatch_event(self.EventTypes.GAME_OVER, {'winner_id': 0})
            return True

        return False



    @staticmethod
    def get_lines_that_include_target_cell(row: int, column: int):

        vertical_line = tuple((row, c) for c in range(3))
        horizontal_line = tuple((r, column) for r in range(3))

        lines = [vertical_line, horizontal_line]

        diagonal_nw_se = ((0, 0), (1, 1), (2, 2))
        diagonal_ne_sw = ((0, 2), (1, 1), (2, 0))

        if (row, column) in diagonal_nw_se:
            lines.append(diagonal_nw_se)
        if (row, column) in diagonal_ne_sw:
            lines.append(diagonal_ne_sw)

        return lines

    def register_event_listener(self, event: str, listener: Callable[[dict[Any, Any]], Any]):
        if event not in self.event_listeners:
            self.event_listeners[event] = set()

        self.event_listeners[event].add(listener)

    def dispatch_event(self, event: str, data: dict = None):
        if event not in self.event_listeners:
            warnings.warn(f"Dispatching '{event}' event, but it has no listeners.")
            return

        if data is None:
            data = {}

        listeners = self.event_listeners[event]

        for listener in listeners:
            print(f"Dispatching '{event}' event with payload {data} to {len(listeners)} listeners.")
            listener(data)


class TicTacToeGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")

        self.logic = None
        self.buttons = {}

        self.initialize_and_start_game()

    def initialize_and_start_game(self):
        self.logic = TicTacToeGameLogic()
        self.initialize_ui()
        self.register_event_listeners()
        self.logic.transition_to_next_turn()

    def initialize_ui(self):
        for row, column in self.logic.cells:
            claim_cell_command = self.claim_cell_command_factory(row, column)
            button = tk.Button(
                self,
                width=3,
                font=Font(size=20, weight='bold'),
                command=claim_cell_command
            )
            button.grid(row=row, column=column)
            self.buttons[row, column] = button

    def register_event_listeners(self):
        self.logic.register_event_listener(
            event=self.logic.EventTypes.CELL_CLAIMED,
            listener=self.update_cell_button_visual
        )

        self.logic.register_event_listener(
            event=self.logic.EventTypes.NEXT_TURN,
            listener=self.try_take_computer_player_turn
        )

        self.logic.register_event_listener(
            event=self.logic.EventTypes.GAME_OVER,
            listener=self.handle_game_over
        )

    def update_cell_button_visual(self, data):
        row, column, player_id = data['row'], data['column'], data['player_id']

        button_to_update: tk.Button = self.buttons[row, column]

        if player_id == 0:
            button_to_update.config(text="", fg="")
        elif player_id == 1:
            button_to_update.config(text="O", fg="green")
        elif player_id == 2:
            button_to_update.config(text="X", fg="red")
        else:
            raise ValueError(f"The given player_id ({player_id}) is invalid. "
                             "It must be 0 (unclaimed), 1 (human), or 2 (computer).}")

    def try_take_computer_player_turn(self, data):
        player_id = 2
        id_of_player_playing_this_turn = data['player_id']
        if player_id != id_of_player_playing_this_turn:
            return

        row, column = random.choice(self.logic.unclaimed_cells)
        self.logic.claim_cell(player_id, row, column)

    def handle_game_over(self, data):
        winner_id = data['winner_id']

        if winner_id == 0:
            player_wants_another_game = askyesno(
                'Draw.', 'The game has ended in a stalemate. Would you like to play again?'
            )
        elif winner_id == 1:
            player_wants_another_game = askyesno(
                'You Win!', 'You are victorious! Would you like to play again?'
            )
        elif winner_id == 2:
            player_wants_another_game = askyesno(
                'You Lose.', 'The computer has vanquished you. Would you like to play again?'
            )
        else:
            raise ValueError(f"The given winner_id ({winner_id}) is invalid. "
                             "It must be 0 (draw), 1 (human wins), or 2 (computer wins).}")

        if player_wants_another_game:
            self.initialize_and_start_game()
        else:
            self.destroy()

    def claim_cell_command_factory(self, row: int, column: int):
        def claim_cell_command():
            try:
                self.logic.claim_cell(player_id=1, row=row, column=column)
            except GameOver as game_over_exc:
                showwarning('Game Over', str(game_over_exc))
            except NotYourTurn as not_your_turn_exc:
                showwarning('Wait Your Turn', str(not_your_turn_exc))
            except CellAlreadyClaimed:
                # Clicking an owned cell should have no effect.
                pass

        return claim_cell_command


if __name__ == '__main__':
    def main():
        TicTacToeGame().mainloop()


    main()
