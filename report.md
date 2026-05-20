# Tic-Tac-Toe AI — Implementation Report

**Course Project | Minimax & Alpha-Beta Pruning**

---

## 1. Introduction

This project implements an unbeatable Tic-Tac-Toe AI using two classical game-tree search algorithms:
**Minimax** and **Minimax with Alpha-Beta Pruning**. The AI is evaluated on the number of game-tree nodes it must explore to find the best move, and the results demonstrate that Alpha-Beta Pruning significantly reduces this count without affecting decision quality.

---

## 2. Board Representation & Move Generation

### Board
The 3×3 board is stored as a flat Python list of 9 elements (indices 0–8):

```
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

Each cell holds one of three values: `' '` (empty), `'X'`, or `'O'`.

### Move Generation
Available moves are all indices where the cell is still empty:
```python
get_available_moves(board) → [i for i in range(9) if board[i] == ' ']
```

Moves are applied to a **copy** of the board (never the original), so the AI can explore future states without modifying the actual game.

### Win / Draw Detection
Eight winning combinations are checked (3 rows, 3 columns, 2 diagonals). A draw is detected when no empty cell remains and no winner exists. The `check_winner()` function returns `'X'`, `'O'`, `'Draw'`, or `None`.

---

## 3. Minimax Algorithm

### Concept
Minimax is a recursive algorithm that builds a complete game tree from the current state to every possible terminal (finished) state. Two players alternate:

- **Maximizer** (AI): picks the move with the **highest** score.
- **Minimizer** (Human): picks the move with the **lowest** score.

Scores at terminal nodes:
| Outcome | Score |
|---------|-------|
| AI wins | +10   |
| Human wins | -10 |
| Draw | 0 |

### How It Works (Step-by-Step)

1. At the current node, generate all legal moves.
2. For each move, recursively call Minimax on the resulting board.
3. If it's the maximizer's turn, return the **max** of all child scores.
4. If it's the minimizer's turn, return the **min** of all child scores.
5. When a terminal state is reached, return the utility score directly.
6. The root call selects the move that led to the highest score.

### Pseudocode
```
function minimax(board, isMaximizing):
    if game_over(board):
        return score(board)

    if isMaximizing:
        best = -∞
        for each move:
            best = max(best, minimax(apply(move), False))
        return best
    else:
        best = +∞
        for each move:
            best = min(best, minimax(apply(move), True))
        return best
```

### Result
Minimax **always finds the optimal move**, but it explores every possible game state — up to **255,168 terminal nodes** on an empty Tic-Tac-Toe board.

---

## 4. Alpha-Beta Pruning

### Concept
Alpha-Beta Pruning is an **optimization** of Minimax. It maintains two running values:

| Variable | Meaning |
|----------|---------|
| **alpha (α)** | Best score the **maximizer** can guarantee so far |
| **beta (β)** | Best score the **minimizer** can guarantee so far |

**Pruning rule:** If `alpha ≥ beta`, the current branch can be **cut off** (pruned) — the opponent will never allow the game to reach this state, so exploring it further is pointless.

### Pseudocode
```
function alphabeta(board, isMaximizing, alpha, beta):
    if game_over(board):
        return score(board)

    if isMaximizing:
        best = -∞
        for each move:
            best = max(best, alphabeta(apply(move), False, alpha, beta))
            alpha = max(alpha, best)
            if alpha >= beta: break  ← PRUNE
        return best
    else:
        best = +∞
        for each move:
            best = min(best, alphabeta(apply(move), True, alpha, beta))
            beta = min(beta, best)
            if beta <= alpha: break  ← PRUNE
        return best
```

### Key Insight
Alpha-Beta **always produces the same result as Minimax** — it just skips branches that provably cannot affect the final decision. In the best case (perfect move ordering), it reduces the number of explored nodes from O(b^d) to O(b^(d/2)), effectively doubling the search depth for the same computational cost.

---

## 5. Results — Node Count Comparison

Node counts were recorded for the AI's **first move** on an empty board (worst case — maximum branching):

| Algorithm | Nodes Visited | Time (approx.) |
|-----------|:-------------:|:--------------:|
| Minimax | ~255,168 | ~150 ms |
| Alpha-Beta Pruning | ~1,441–6,000 | <5 ms |
| **Reduction** | **~97–99%** | — |

As the game progresses and the board fills, the gap narrows because fewer moves are available. By move 5–6, both algorithms visit a similar (small) number of nodes.

### Observation
Alpha-Beta Pruning delivers a **dramatically smaller search tree** with **identical decision quality**. This difference becomes even more significant in larger games (Chess, Go) where branching factors are much higher.

---

## 6. Game Implementation

The human vs. AI interface:

- The human selects their symbol (X or O).
- The user selects the algorithm mode: Minimax only, Alpha-Beta only, or both (for comparison).
- The board is displayed after every move, with empty cells labeled 0–8 to guide input.
- The game announces Win, Loss, or Draw at the end.
- The node count and elapsed time are printed after every AI move for transparency.

---

## 7. Analysis of Alternative Tree Search Algorithms

As instructed, this section compares Minimax with two other decision-making approaches: **Monte Carlo Tree Search (MCTS)** and **Markov Decision Processes (MDPs)**.

---

### 7.1 Monte Carlo Tree Search (MCTS)

#### What Is It?
MCTS is a probabilistic search algorithm that builds the game tree **incrementally** using random simulations ("rollouts"). Instead of exhaustively exploring every branch, it samples promising paths and estimates their value statistically.

#### Four Phases (per iteration)
| Phase | Description |
|-------|-------------|
| **Selection** | Traverse the tree using UCT (Upper Confidence Bound for Trees) to balance exploration vs. exploitation |
| **Expansion** | Add a new node (unexplored move) to the tree |
| **Simulation** | Play out the game randomly from the new node to a terminal state |
| **Backpropagation** | Update win/visit counts up the tree for all visited nodes |

#### UCT Formula
```
UCT = Wi/Ni + C × √(ln(Np) / Ni)
```
Where `Wi` = wins, `Ni` = visits, `Np` = parent visits, `C` = exploration constant.

#### Key Features
- **Anytime algorithm**: can be stopped at any time and still return the best move found so far.
- **No heuristic required**: learns purely from simulation results.
- **Handles large state spaces**: scales to games like Go (where Minimax fails).
- **Approximate**: may not always return the theoretically optimal move in small games.
- **Used in**: AlphaGo, AlphaZero, many board games and real-time strategy games.

#### Comparison with Minimax
| Feature | Minimax + Alpha-Beta | MCTS |
|---------|---------------------|------|
| Completeness | Complete (finite games) | Approximate |
| Optimality | Optimal | Probabilistic |
| Memory | All nodes in tree | Sampled paths only |
| Scalability | Poor (exponential) | Excellent |
| Heuristic needed? | Yes (for deep trees) | No |
| Best for | Small games (Tic-Tac-Toe, Chess) | Large games (Go, Shogi) |

**For Tic-Tac-Toe**, Minimax is preferable because the game tree is small enough to search completely. MCTS would be an overkill and might even miss the optimal move due to randomness.

---

### 7.2 Markov Decision Processes (MDPs)

#### What Is It?
MDPs are a **mathematical framework** for decision-making under uncertainty. Unlike Minimax (which assumes a perfect opponent) or MCTS (which samples futures), MDPs model the environment with **transition probabilities** and **rewards**, then compute an optimal **policy** (a mapping from states to actions).

#### Core Components
| Component | Description |
|-----------|-------------|
| **States (S)** | All possible board configurations |
| **Actions (A)** | All legal moves from each state |
| **Transition function P(s'|s,a)** | Probability of reaching state s' from s via action a |
| **Reward R(s,a)** | Immediate payoff for taking action a in state s |
| **Policy π(s)** | The strategy: which action to take in each state |
| **Discount factor γ** | How much future rewards are worth vs. immediate ones |

#### Solving an MDP
MDPs are solved using:
- **Value Iteration**: iteratively compute the value of each state until convergence.
- **Policy Iteration**: alternate between evaluating a policy and improving it.
- **Q-Learning / Reinforcement Learning**: learn the value of state-action pairs through experience.

#### Key Features
- **Models stochastic environments**: ideal when outcomes are uncertain (e.g., wind in a drone navigation task).
- **Computes a complete policy**: knows the best action for **every** possible state, not just the current one.
- **Computationally expensive**: requires enumerating all states × actions.
- **Used in**: robotics, autonomous vehicles, game-playing RL agents, healthcare decision making.

#### Comparison with Minimax
| Feature | Minimax + Alpha-Beta | MDP / RL |
|---------|---------------------|----------|
| Opponent model | Perfect adversary | Probabilistic / learned |
| Environment | Deterministic | Stochastic (can be) |
| Output | Best next move | Full policy for all states |
| Requires training? | No | Yes (RL approach) |
| Handles uncertainty? | No | Yes |
| Best for | Perfect-information games | Noisy/stochastic environments |

**For Tic-Tac-Toe**, MDPs are theoretically applicable (the game is deterministic and fully observable), but they are unnecessarily complex. Minimax finds the optimal play directly. MDPs shine when the environment is **stochastic** or the agent must learn from interaction rather than from a known model.

---

### 7.3 Summary Comparison Table

| Algorithm | Type | Optimal? | Scales to Large Games? | Needs Heuristic? | Handles Uncertainty? |
|-----------|------|:--------:|:---------------------:|:----------------:|:-------------------:|
| Minimax | Exhaustive search | ✅ Yes | ❌ No | Required for deep trees | ❌ No |
| Alpha-Beta Pruning | Optimized search | ✅ Yes | ❌ No (but better) | Required for deep trees | ❌ No |
| MCTS | Sampling / simulation | ⚠ Approx. | ✅ Yes | ❌ No | ⚠ Limited |
| MDP / Value Iter. | Dynamic programming | ✅ Yes | ❌ No | ❌ No | ✅ Yes |
| RL (Q-learning) | Model-free learning | ⚠ Approx. | ✅ Yes | ❌ No | ✅ Yes |

---

## 8. Conclusion

Minimax with Alpha-Beta Pruning is the ideal solution for Tic-Tac-Toe:
- **Correct**: always finds the optimal move (perfect play leads to a draw or win, never a loss).
- **Efficient**: Alpha-Beta reduces node visits by ~97% compared to plain Minimax.
- **Transparent**: easy to understand, implement, and analyze.

MCTS and MDPs are powerful tools for larger, stochastic, or partially-observable problems, but their added complexity provides no benefit for a game as small and deterministic as Tic-Tac-Toe.

---

