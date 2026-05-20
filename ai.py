"""
Tic-Tac-Toe AI | AI Algorithms
==============================
Minimax and Alpha-Beta Pruning decision logic.
"""
import math
from board import get_available_moves, make_move, is_terminal, get_score

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
