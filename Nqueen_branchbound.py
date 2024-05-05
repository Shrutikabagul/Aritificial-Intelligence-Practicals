class NQueens:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def is_safe(self, board, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(self, board, row):
        if row == self.n:
            self.solutions.append(board[:])
            return

        for col in range(self.n):
            if self.is_safe(board, row, col):
                board[row] = col
                self.solve(board, row + 1)
                board[row] = -1

    def branch_and_bound(self):
        board = [-1] * self.n
        self.solve(board, 0)
        return self.solutions

    def print_solution(self, solution):
        for row in solution:
            line = ['.'] * self.n
            line[row] = 'Q'
            print(''.join(line))

# Example usage
n = 5 # Number of queens
n_queens = NQueens(n)
solutions = n_queens.branch_and_bound()
print("Solutions for", n, "queens:")
for solution in solutions:
    n_queens.print_solution(solution)
    print()
