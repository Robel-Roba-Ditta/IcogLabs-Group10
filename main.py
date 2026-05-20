"""
Tic-Tac-Toe AI | Main Entry Point
=================================
Game loop, user input, and algorithm comparison.
"""
import time
from board import create_board, make_move, check_winner
from ai import get_best_move_minimax, get_best_move_alpha_beta
from ui import bold, dim, green, cyan, print_board

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
    print(f"  {bold('│')}{cyan('ALGORITHM COMPARISON — Node Count & Time'):^{W+len(cyan(''))}}{bold('│')}")
    print(f"  {bold('├' + '─'*18 + '┬' + '─'*17 + '┬' + '─'*17 + '┤')}")
    print(f"  {bold('│')} {'Algorithm':<16} {bold('│')} {'Nodes Visited':>15} {bold('│')} {'Time (ms)':>15} {bold('│')}")
    print(f"  {bold('├' + '─'*18 + '┼' + '─'*17 + '┼' + '─'*17 + '┤')}")
    print(f"  {bold('│')} {'Minimax':<16} {bold('│')} {bold(f'{nodes_mm:>15,}')} {bold('│')} {bold(f'{time_mm:>15.3f}')} {bold('│')}")
    print(f"  {bold('│')} {'Alpha-Beta':<16} {bold('│')} {bold(f'{nodes_ab:>15,}')} {bold('│')} {bold(f'{time_ab:>15.3f}')} {bold('│')}")
    print(f"  {bold('├' + '─'*18 + '┴' + '─'*17 + '┴' + '─'*17 + '┤')}")
    
    nodes_str = f"Nodes pruned : {reduction:.1f}%"
    speedup_str = f"Speedup : {time_mm/time_ab:.1f}x faster" if time_ab > 0 else ""
    if speedup_str:
        bottom_plain = f"  {nodes_str}   |   {speedup_str}"
        bottom_colored = f"  {green(nodes_str)}   |   {green(speedup_str)}"
    else:
        bottom_plain = f"  {nodes_str}"
        bottom_colored = f"  {green(nodes_str)}"
        
    padding = " " * max(0, W - len(bottom_plain))
    print(f"  {bold('│')}{bottom_colored}{padding}{bold('│')}")
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
    try:
        while True:
            play_game()
            if input("  Play again? (y/n): ").strip().lower() != 'y':
                print(f"\n  {dim('Goodbye!')}\n")
                break
    except KeyboardInterrupt:
        print(f"\n  {dim('Goodbye!')}\n")
