"""
Tic-Tac-Toe AI  |  Minimax + Alpha-Beta Pruning
================================================
Author : Robel Roba
Topic  : Minimax + Alpha-Beta Pruning

"""
import math
import time

BOLD  = "\033[1m"
DIM   = "\033[2m"
GREEN = "\033[92m"
CYAN  = "\033[96m"
RESET = "\033[0m"

def bold(text):   return f"{BOLD}{text}{RESET}"
def dim(text):    return f"{DIM}{text}{RESET}"
def green(text):  return f"{GREEN}{BOLD}{text}{RESET}"
def cyan(text):   return f"{CYAN}{text}{RESET}"

WIN_CONDITIONS = [
    [0,1,2], [3,4,5], [6,7,8],   
    [0,3,6], [1,4,7], [2,5,8],   
    [0,4,8], [2,4,6]             
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

def minimax(board, is_maximizing, ai_player, human_player, node_count):
    node_count[0] += 1
    if is_terminal(board):
        return get_score(board, ai_player, human_player)
    moves = get_available_moves(board)
    if is_maximizing:
        best = -math.inf
        for move in moves:
            score = minimax(make_move(board, move, ai_player), False, ai_player, human_player, node_count)
            best = max(best, score)
        return best
    else:
        best = math.inf
        for move in moves:
            score = minimax(make_move(board, move, human_player), True, ai_player, human_player, node_count)
            best = min(best, score)
        return best

def get_best_move_minimax(board, ai_player, human_player):
    best_score, best_move, node_count = -math.inf, None, [0]
    for move in get_available_moves(board):
        score = minimax(make_move(board, move, ai_player), False, ai_player, human_player, node_count)
        if score > best_score:
            best_score, best_move = score, move
    return best_move, node_count[0]

def minimax_alpha_beta(board, is_maximizing, ai_player, human_player, alpha, beta, node_count):
    node_count[0] += 1
    if is_terminal(board):
        return get_score(board, ai_player, human_player)
    moves = get_available_moves(board)
    if is_maximizing:
        best = -math.inf
        for move in moves:
            score = minimax_alpha_beta(make_move(board, move, ai_player), False, ai_player, human_player, alpha, beta, node_count)
            best = max(best, score)
            alpha = max(alpha, score)
            if alpha >= beta:
                break
        return best
    else:
        best = math.inf
        for move in moves:
            score = minimax_alpha_beta(make_move(board, move, human_player), True, ai_player, human_player, alpha, beta, node_count)
            best = min(best, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best

def get_best_move_alpha_beta(board, ai_player, human_player):
    best_score, best_move, node_count = -math.inf, None, [0]
    for move in get_available_moves(board):
        score = minimax_alpha_beta(make_move(board, move, ai_player), False, ai_player, human_player, -math.inf, math.inf, node_count)
        if score > best_score:
            best_score, best_move = score, move
    return best_move, node_count[0]

def compare_algorithms(board, ai_player, human_player):
    t1 = time.perf_counter()
    _, nodes_mm = get_best_move_minimax(board, ai_player, human_player)
    t2 = time.perf_counter()
    t3 = time.perf_counter()
    _, nodes_ab = get_best_move_alpha_beta(board, ai_player, human_player)
    t4 = time.perf_counter()

    time_mm   = (t2 - t1) * 1000
    time_ab   = (t4 - t3) * 1000
    reduction = (1 - nodes_ab / nodes_mm) * 100 if nodes_mm > 0 else 0

    W = 54
    print(f"\n  {bold('┌' + '─' * W + '┐')}")
    print(f"  {bold('│'):}{cyan('  ALGORITHM COMPARISON — Node Count & Time'):^{W+len(cyan(''))}}{bold('│')}")
    print(f"  {bold('├' + '─'*16 + '┬' + '─'*14 + '┬' + '─'*12 + '┬' + '─'*(W-16-14-12-2) + '┤')}")
    print(f"  {bold('│')} {'Algorithm':<14} {bold('│')} {'Nodes Visited':>12} {bold('│')} {'Time (ms)':>10} {bold('│')} {'':^7} {bold('│')}")
    print(f"  {bold('├' + '─'*16 + '┼' + '─'*14 + '┼' + '─'*12 + '┼' + '─'*(W-16-14-12-2) + '┤')}")
    print(f"  {bold('│')} {'Minimax':<14} {bold('│')} {bold(f'{nodes_mm:>12,}')} {bold('│')} {bold(f'{time_mm:>10.3f}')} {bold('│')} {'':^7} {bold('│')}")
    print(f"  {bold('│')} {'Alpha-Beta':<14} {bold('│')} {bold(f'{nodes_ab:>12,}')} {bold('│')} {bold(f'{time_ab:>10.3f}')} {bold('│')} {'':^7} {bold('│')}")
    print(f"  {bold('├' + '─'*16 + '┴' + '─'*14 + '┴' + '─'*12 + '┴' + '─'*(W-16-14-12-2) + '┤')}")
    print(f"  {bold('│')}  {green(f'Nodes pruned : {reduction:.1f}%')}   |   {green(f'Speedup : {time_mm/time_ab:.1f}x faster') if time_ab > 0 else '':<30}{'':<{W - 52}}  {bold('│')}")
    print(f"  {bold('└' + '─' * W + '┘')}\n")


def get_human_move(board):
    while True:
        try:
            move = int(input("  Your move (0-8): "))
            if 0 <= move <= 8 and board[move] == ' ':
                return move
            print("  Invalid move. Try again.")
        except ValueError:
            print("  Enter a number between 0 and 8.")

def play_game():
    print(f"\n  {bold('=' * 50)}")
    print(f"  {bold('    TIC-TAC-TOE  —  Minimax + Alpha-Beta AI')}")
    print(f"  {bold('=' * 50)}")

    while True:
        symbol = input("\n  Play as X (first) or O (second)? ").strip().upper()
        if symbol in ('X', 'O'):
            break
        print("  Enter X or O.")

    human_player = symbol
    ai_player = 'O' if human_player == 'X' else 'X'

    print(f"\n  Algorithm:  {bold('[1] Minimax')}  {bold('[2] Alpha-Beta')}  {bold('[3] Both (compare)')}")
    while True:
        choice = input("  Enter 1, 2, or 3: ").strip()
        if choice in ('1', '2', '3'):
            break
        print("  Enter 1, 2, or 3.")

    board = create_board()
    current_player = 'X'
    print(f"\n  You = {bold(human_player)}  |  AI = {bold(ai_player)}\n")

    while True:
        print_board(board)
        if check_winner(board) is not None:
            break

        if current_player == human_player:
            print(f"  {bold('YOUR TURN')} ('{human_player}')")
            move = get_human_move(board)
            board = make_move(board, move, human_player)
        else:
            print(f"  {dim('AI thinking...')} ('{ai_player}')")
            if choice == '1':
                move, nodes = get_best_move_minimax(board, ai_player, human_player)
                print(f"  AI played {bold(move)}  |  Minimax nodes visited: {bold(f'{nodes:,}')}")
            elif choice == '2':
                move, nodes = get_best_move_alpha_beta(board, ai_player, human_player)
                print(f"  AI played {bold(move)}  |  Alpha-Beta nodes visited: {bold(f'{nodes:,}')}")
            else:
                compare_algorithms(board, ai_player, human_player)
                move, _ = get_best_move_alpha_beta(board, ai_player, human_player)
                print(f"  AI played {bold(move)}")
            board = make_move(board, move, ai_player)

        current_player = 'O' if current_player == 'X' else 'X'

    print_board(board)
    result = check_winner(board)
    print(f"  {bold('=' * 50)}")
    if result == 'Draw':
        print(f"  {bold('  Draw! Well played.')}")
    elif result == human_player:
        print(f"  {green('  You win! Impressive.')}")
    else:
        print(f"  {bold('  AI wins! Better luck next time.')}")
    print(f"  {bold('=' * 50)}\n")

if __name__ == "__main__":
    while True:
        play_game()
        if input("  Play again? (y/n): ").strip().lower() != 'y':
            print(f"\n  {dim('Goodbye!')}\n")
            break
