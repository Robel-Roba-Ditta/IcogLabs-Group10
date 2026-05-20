"""
Tic-Tac-Toe AI | UI Utilities
=============================
ANSI escape codes, string styling, and board printing logic.
"""

BOLD  = "\033[1m"
DIM   = "\033[2m"
GREEN = "\033[92m"
CYAN  = "\033[96m"
RESET = "\033[0m"

def bold(text):   return f"{BOLD}{text}{RESET}"
def dim(text):    return f"{DIM}{text}{RESET}"
def green(text):  return f"{GREEN}{BOLD}{text}{RESET}"
def cyan(text):   return f"{CYAN}{text}{RESET}"

def print_board(board):
    print()
    for row in range(3):
        cells = [dim(str(row*3+col)) if board[row*3+col] == ' '
                 else bold(board[row*3+col])
                 for col in range(3)]
        print(f"  {cells[0]} | {cells[1]} | {cells[2]}")
        if row < 2:
            print(f"  {dim('--+---+--')}")
    print()
