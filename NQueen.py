#self.n: Stores the number of queens.
#self.board: Represents the chessboard as a list of length n, initialized with -1.
#self.solutions: Stores the solutions found, initialized as an empty list.
#Base case: If row equals n, all queens have been successfully placed on the board, so the current configuration is added to self.solutions.
class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solutions = []

#same col,same row ,diagonally threatning 
    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
               self.board[i] - i == col - row or \
               self.board[i] + i == col + row:
                return False
        return True

    def solve(self, row=0):
        if row == self.n:
            self.solutions.append(self.board[:])
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.solve(row + 1)
                self.board[row] = -1

    def print_solutions(self):
        for solution in self.solutions:
            for row in solution:
                line = ['.'] * self.n
                line[row] = 'Q'
                print(''.join(line))
            print()

# Example usage
n = 4  # Number of queens
n_queens = NQueens(n)
n_queens.solve()
print("Solutions for", n, "queens:")
n_queens.print_solutions()
