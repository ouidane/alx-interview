#!/usr/bin/python3
"""
Solves the N Queens problem using backtracking.
"""

import sys


def is_safe(queen_positions, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for r in range(row):
        c = queen_positions[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row=0, queen_positions=[], solutions=[]):
    """Recursively solve the N Queens problem."""
    if row == n:
        solutions.append([[r, queen_positions[r]] for r in range(n)])
        return

    for col in range(n):
        if is_safe(queen_positions, row, col):
            queen_positions.append(col)
            solve_nqueens(n, row + 1, queen_positions, solutions)
            queen_positions.pop()


def main():
    """Entry point for the N Queens script."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(n, queen_positions=[], solutions=solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
