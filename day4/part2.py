#!/usr/bin/env python3

class Board:
    def __init__(self, lines):
        self.grid = []
        self.won = False
        for line in lines:
            if line == '': continue
            self.grid.append([int(i) for i in line.split()])

    def check_number(self, number):
        for i in range(5):
            for j in range(5):
                if self.grid[i][j] == number:
                    self.grid[i][j] = None
                    break

        # any column all set
        for i in range(5):
            col_set = True
            for j in range(5):
                if self.grid[j][i] != None:
                    col_set = False
                    break
            if col_set:
                self.won = True
                return True

        # any row all set
        for i in range(5):
            row_set = True
            for j in range(5):
                if self.grid[i][j] != None:
                    row_set = False
                    break
            if row_set:
                self.won = True
                return True

        # No Bingo yet
        return False

    def sum_unchecked(self):
        total_sum = 0
        for i in range(5):
            for j in range(5):
                if self.grid[i][j] is not None:
                    total_sum += self.grid[i][j]
        return total_sum

    def __str__(self):
        return '\n'.join([str(row) for row in self.grid])


if __name__ == '__main__':
    data = open('input').read().splitlines()

    # Load Bingo numbers
    numbers = [int(i) for i in data[0].split(',')]

    # Load Bingo boards
    boards = []
    for i in range(2, len(data), 6):
        boards.append(Board(data[i:i + 6]))
        print('--- Board ---')
        print(boards[-1])

    # Play Bingo
    boards_in_play = len(boards)
    for number in numbers:
        for i,board in enumerate(boards):
            if board.won: continue
            if board.check_number(number):
                if boards_in_play > 1:
                    boards_in_play -= 1
                    print(f'Winning board found, new boards in play: {boards_in_play}')
                else:
                    print('--- Winning Board ---')
                    print(board)
                    boardsum = board.sum_unchecked()
                    print(f'BINGO: {boardsum} * {number} == {boardsum * number}')
                    exit()
