from typing import List, Dict, Tuple

class Table:
    def __init__(self, contents: List[List[int]]):
        self.grid: List[List[int]] = contents

    def get_square(self, square_num: int) -> List[int]:
        """
          Possible square numbers:
              1 2 3
              4 5 6
              7 8 9
        """
        
        # Get the starting row and column for the square
        row_start = (square_num - 1) // 3 * 3
        col_start = (square_num - 1) % 3 * 3

        # Get the square
        square = []
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                square.append(self.grid[row][col])

        return square

    def get_row(self, row_num: int) -> List[int]:
        return self.grid[row_num]

    def get_col(self, col_num: int) -> List[int]:
        return [row[col_num] for row in self.grid]

    def is_valid_structure(self, struct: List[int]) -> bool:
        """ Checks if a structure is valid (no duplicates) """
        # NOTE: A structure is a row, column, or square

        logs = []

        for item in struct:
            logs.append(struct.count(item) == 1)

        return all(logs)

    def is_valid_table(self) -> bool:
        """ Checks the entire table for validity """

        for i in range(9):
            if not self.is_valid_structure(self.get_row(i)):
                return False
            if not self.is_valid_structure(self.get_col(i)):
                return False
            if not self.is_valid_structure(self.get_square(i)):
                return False

        return True

    def calculate_av_nums_for_cell(self, row: int, col: int) -> List[int]:
        """ Calculates the available numbers for a cell """

        # Get the numbers in the row, column, and square
        row_nums = self.get_row(row)
        col_nums = self.get_col(col)
        square_nums = self.get_square((row // 3) * 3 + (col // 3) + 1)

        # Get the available numbers
        av_nums: List[int] = list(range(1, 10))
        for num in row_nums + col_nums + square_nums:
            if num in av_nums:
                av_nums.remove(num)

        return av_nums

    def find_empty_cells(self) -> List[Tuple[int, int]]:
        """ Finds the empty cells in the table """

        empty_cells: List[Tuple[int, int]] = []

        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    empty_cells.append((row, col))

        return empty_cells

    def solve(self):
        empty_cells = self.find_empty_cells()
        was_changed = False

        # If there are no empty cells, the table is solved
        if len(empty_cells) == 0:
            return

        # For each empty cell, calculate the available numbers
        # If there is only one available number, fill it in

        for (row, col) in empty_cells:
            av_nums = self.calculate_av_nums_for_cell(row, col)

            if len(av_nums) == 1:
                was_changed = True
                self.grid[row][col] = av_nums[0]

        if was_changed:
            self.solve()
        else:
            print("Sorry, I couldn't solve this one :(")
            # TODO: Implement backtracking algorithm

def get_table() -> Table:
    print('Enter a Sudoku:')
    table = [list(map(int, list(input()))) for _ in range(9)]
    return Table(table)

def create_table_representation(table: Table, is_solved: bool) -> List[str]:
    table_repr: List[str] = []

    header = '+---------FINAL---------+' if is_solved else '+----------RAW----------+'
    table_repr.append(header)

    for row in range(9):
        first_sq, second_sq, third_sq = ' '.join(map(str, table.grid[row][:3])), ' '.join(map(str, table.grid[row][3:6])), ' '.join(map(str, table.grid[row][6:]))
        table_repr.append(f'| {first_sq} | {second_sq} | {third_sq} |')

        if row in [2, 5]:
            table_repr.append("| - - - + - - - + - - - |")

    table_repr.append(header)

    return table_repr

def print_tables_combined(unsolved: Table, solved: Table):
    unsolved_repr = create_table_representation(unsolved, False)
    solved_repr = create_table_representation(solved, True)

    for i in range(len(unsolved_repr)):
        print(f'{unsolved_repr[i]} {solved_repr[i]}')
