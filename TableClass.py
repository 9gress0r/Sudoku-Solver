class Table:

    def __init__(self, table):
        self.table = table
        self.pos_nums = list(range(1, 10))

    def __call__(self):
        return self.table

    def get_square(line1, line2, line3, num):
        """ Getting a square """

        square = []

        if num == 1:
            for index in range(3):
                square.append(line1[index])
                square.append(line2[index])
                square.append(line3[index])

        elif num == 2:
            for index in range(3, 6):
                square.append(line1[index])
                square.append(line2[index])
                square.append(line3[index])

        elif num == 3:
            for index in range(6, 9):
                square.append(line1[index])
                square.append(line2[index])
                square.append(line3[index])

        return square

    def get_ver_line(self, num):
        """ Getting a vertical line """

        return [item[num] for item in self.table]

    def get_hor_line(self, row):
        """
        Gets all numbers in a horizontal line by a number and turn it into the array
        """

        return self.table[row]

    def is_validLine(self, line):
        """ Checks is a line valid """

        logs = []

        for item in self.pos_nums:
            if line.count(item) == 1:
                logs.append(True)
            else:
                logs.append(False)

        return all(logs)

    def is_validSquare(self, square):
        """ Checks is a square valid """

        logs = []

        for item in self.pos_nums:
            if square.count(item) == 1:
                logs.append(True)
            else:
                logs.append(False)

        return all(logs)

    def check_vertical_lines(self):
        """ Checks all vertical lines in a table """

        logs = [self.is_validLine(self.get_ver_line(self.table, col)) for col in range(9)]

        return all(logs)

    def check_horizontal_lines(self):
        """ Checks all horizontal lines in a table """

        logs = [self.is_validLine(line) for line in self.table]

        return all(logs)

    def check_squares(self):
        """ Checks all squares in a table """

        logs = []

        for item in range(0, 7, 3):
            line1, line2, line3 = self.table[item], self.table[item + 1], self.table[item + 2]
            for num in range(1, 4):
                square = self.get_square(line1, line2, line3, num)
                logs.append(self.is_validSquare(square))

        return all(logs)

    def is_validTable(self):
        """ Checks is a table valid """

        logs = [self.check_vertical_lines(self.table), self.check_horizontal_lines(self.table), self.check_squares(self.table)]

        return all(logs)

    def get_sq(self, num):
        """
        Gets all numbers in a square by a number and turn it into the array
        """

        square = []

        if num in [1, 2, 3]:
            for row in range(3):
                if num == 1:
                    square.extend(self.table[row][:3])
                elif num == 2:
                    square.extend(self.table[row][3:6])
                elif num == 3:
                    square.extend(self.table[row][6:9])

        elif num in [4, 5, 6]:
            for row in range(3, 6):
                if num == 4:
                    square.extend(self.table[row][:3])
                elif num == 5:
                    square.extend(self.table[row][3:6])
                elif num == 6:
                    square.extend(self.table[row][6:9])

        elif num in [7, 8, 9]:
            for row in range(6, 9):
                if num == 7:
                    square.extend(self.table[row][:3])
                elif num == 8:
                    square.extend(self.table[row][3:6])
                elif num == 9:
                    square.extend(self.table[row][6:9])

        return square

    def available_nums(self, row, col):
        """
        Returns an array of available numbers for given cell
        """

        hor, ver, sq = self.get_hor_line(row), self.get_ver_line(col), list()

        if row in range(3):
            if col in range(3):
                sq = self.get_sq(1)
            elif col in range(3, 6):
                sq = self.get_sq(2)
            elif col in range(6, 9):
                sq = self.get_sq(3)

        elif row in range(3, 6):
            if col in range(3):
                sq = self.get_sq(4)
            elif col in range(3, 6):
                sq = self.get_sq(5)
            elif col in range(6, 9):
                sq = self.get_sq(6)

        elif row in range(6, 9):
            if col in range(3):
                sq = self.get_sq(7)
            elif col in range(3, 6):
                sq = self.get_sq(8)
            elif col in range(6, 9):
                sq = self.get_sq(9)

        return [
            item for item in self.pos_nums
            if item not in hor and item not in ver and item not in sq
        ]

    def find_holes(self):
        """
        Returns an array of indexes of cells that can be changed
        """

        result = []

        for row in range(len(self.table)):
            for col in range(len(self.table[row])):
                if self.table[row][col] == 0:
                    result.append((row, col))

        return result

    def solve(self):
        """
        Main function for solving a table
        """

        holes = {(row, col): self.available_nums(row, col) for row, col in self.find_holes()}
        was_changed = False

        for key, val in holes.items():
            if len(val) == 1:
                was_changed = True

                row, col = key
                self.table[row][col] = val[0]

        if was_changed:
            self.solve()

        return self.table
