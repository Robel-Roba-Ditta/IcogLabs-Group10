"""
Tic-Tac-Toe AI | Board and Rules
================================
Core game logic and state management.
"""

WIN_CONDITIONS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def create_board():
    return [' '] * 9

def get_available_moves(board):
    return [i for i in range(9) if board[i] == ' ']

def make_move(board, position, player):
    new_board = board[:]
    new_board[position] = player
    return new_board

def check_winner(board):
    for a, b, c in WIN_CONDITIONS:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    if ' ' not in board:
        return 'Draw'
    return None

def is_terminal(board):
    return check_winner(board) is not None

def get_score(board, ai_player, human_player):
    winner = check_winner(board)
    if winner == ai_player:    return 10
    if winner == human_player: return -10
    return 0
