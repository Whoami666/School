import os
import sys
import pickle
from random import randrange
from typing import List, Optional, Tuple, Set


class Game:
    def __init__(self, rows, columns, mines):
        self.rows = rows
        self.columns = columns
        self.n_mines = mines
        self.full_board = [[0 for _ in range(columns)] for _ in range(rows)]

        self.generate_board(rows, columns, mines)

        self.view_board = [["x" for _ in range(columns)] for _ in range(rows)]

    def print_view_board(self):
        print("_" * 5 + "_".join([str(k) for k in range(0, min(self.columns, 10))]))
        for i in range(self.rows):
            print(f"{str(i).zfill(3)}|", *self.view_board[i])

    def print_full_board(self):
        print("_" * 5 + "_".join([str(k) for k in range(0, min(self.columns, 10))]))
        for i in range(self.rows):
            viewable_row = []
            for elem in self.full_board[i]:
                if elem == -1:
                    viewable_row.append("b")
                else:
                    viewable_row.append(str(elem))

            print(f"{str(i).zfill(3)}|", *viewable_row)

    def check_board(self):
        closed_cells = 0
        for row in self.view_board:
            closed_cells += row.count("x") + row.count("f")

        if closed_cells == self.n_mines:
            self.print_full_board()
            print("You won!")
            raise EndgameException()

    def open_cell(self, x, y, opened = None) -> bool:
        if opened is None:
            opened = set()

        if self.full_board[x][y] == -1:
            return False

        self.view_board[x][y] = str(self.full_board[x][y])

        opened.add((x, y,))

        if self.full_board[x][y] == 0:
            adjacent_cells = self.get_adjacent(x, y)
            for cell in adjacent_cells:
                if cell not in opened:
                    self.open_cell(*cell, opened)

        return True

    def flag_cell(self, x, y):
        if self.view_board[x][y] != "x":
            return
        
        self.view_board[x][y] = "f"

    def generate_board(self, rows, columns, mines):
        indices: Set[Tuple[int, int]] = set()
        while len(indices) != mines:
            indices.add(
                (
                    randrange(0, rows),
                    randrange(0, columns),
                )
            )

        for elem in indices:
            # let -1 be bomb
            self.full_board[elem[0]][elem[1]] = -1

        for i in range(rows):
            for j in range(columns):
                if self.full_board[i][j] == -1:
                    continue

                adjacent_cells = self.get_adjacent(i, j)
                n_bombs = 0
                for cell in adjacent_cells:
                    if self.full_board[cell[0]][cell[1]] == -1:
                        n_bombs += 1

                self.full_board[i][j] = n_bombs

    def get_adjacent(self, row, col) -> List[Tuple[int, int]]:
        adjacent_cells = []
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < self.rows and 0 <= j < self.columns:
                    adjacent_cells.append(
                        (
                            i,
                            j,
                        )
                    )

        return adjacent_cells

    def parse_input(self):
        def die():
            print(
                f"Could not parse input. Usage:\nOpen row col - open cell\nFlag row col - flag cell\n0 <= col <= {self.columns-1}\n0 <= row <= {self.rows-1}"
            )

        while True:
            cmd = input("$ ").split()
            if len(cmd) != 3:
                die()
                continue

            if cmd[0].lower() not in ("open", "flag"):
                die()
                continue

            if (not 0 <= int(cmd[1]) <= self.rows - 1) or (
                not 0 <= int(cmd[2]) <= self.columns - 1
            ):
                die()
                continue

            return (
                cmd[0].lower(),
                int(cmd[1]),
                int(cmd[2]),
            )

    def tick(self):
        self.print_view_board()
        action, x, y = self.parse_input()
        if action == "open":
            res = self.open_cell(x, y)
            if not res:
                print("Bad luck dude")
                self.print_full_board()
                raise EndgameException()
        else:
            self.flag_cell(x, y)

        self.check_board()

    def save_game(self):
        f = open("minesweeper_save.pickle", "wb")
        pickle.dump(self, f)


class EndgameException(Exception):
    pass


def try_load_game() -> Optional[Game]:
    if "minesweeper_save.pickle" in os.listdir():
        f = open("minesweeper_save.pickle", "rb")
        d = f.read()
        game = pickle.loads(d)
        return game
    
    return None


if __name__ == "__main__":
    game = try_load_game()
    if game is None:
        rows = int(input("Enter the amount of rows in game: "))
        if rows <= 0:
            print("Amount of rows must be 1 or greater")
            sys.exit()
        columns = int(input("Enter the amount of columns in the game: "))
        if columns <= 0:
            print("Amount of columns must be 1 or greater")
            sys.exit()
        mines = int(input("Enter the amount of mines: "))
        if mines < 0:
            print("Amount of mines cannot be negative")
            sys.exit()

        game = Game(rows, columns, mines)
    else:
        print("Loaded save, delete minesweeper_save.pickle or end this game to start a new one")

    while True:
        try:
            game.tick()
        except EndgameException:
            if "minesweeper_save.pickle" in os.listdir():
                os.remove("minesweeper_save.pickle")
            sys.exit()
        except KeyboardInterrupt:
            print("Saved game state to minesweeper_save.pickle")
            game.save_game()
            sys.exit()
