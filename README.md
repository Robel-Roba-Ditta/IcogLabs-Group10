<div align="center">

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║        ✕  ─────────────  ○  ─────────────  ✕             ║
║        │   TIC · TAC · TOE   A I   ENGINE  │             ║
║        ○  ─────────────  ✕  ─────────────  ○             ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

# Tic-Tac-Toe AI Engine
### Minimax · Alpha-Beta Pruning · Game Tree Analysis

<br>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Algorithm](https://img.shields.io/badge/Algorithm-Minimax-FF6B35?style=for-the-badge)](/)
[![Pruning](https://img.shields.io/badge/Pruning-Alpha--Beta-22C55E?style=for-the-badge)](/)
[![License](https://img.shields.io/badge/License-MIT-A855F7?style=for-the-badge)](/)
[![Status](https://img.shields.io/badge/Status-Complete-14B8A6?style=for-the-badge)](/)

<br>

> *"Every board state explored. Every branch pruned. The AI never loses."*

<br>

</div>

---

## ◈ What Is This?

This project implements an **unbeatable Tic-Tac-Toe AI** built from scratch in Python — no libraries, no shortcuts. The AI uses two classical game-tree search algorithms and pits them head-to-head, proving that **Alpha-Beta Pruning achieves the same perfect play as Minimax while visiting ~94% fewer nodes**.

Built as part of an AI course project exploring adversarial search, the codebase is deeply commented and designed to be readable by complete beginners.

---

## ◈ The Board

```
 0 | 1 | 2       X | 1 | 2       X | O | X
---+---+---     ---+---+---     ---+---+---
 3 | 4 | 5  →   3 | O | 5  →   X | O | O
---+---+---     ---+---+---     ---+---+---
 6 | 7 | 8       6 | 7 | 8       O | X | X

  [empty]        [mid-game]     [AI wins ✕]
```

The board is represented as a flat list of 9 cells. Empty cells show their index (0–8) so the human player always knows where to play.

---

## ◈ Algorithms Implemented

### 01 · Minimax

```
                    [Root]
                   AI plays
                  /    |    \
               [0]    [4]   [8]     ← AI's possible moves
               / \    / \   / \
             ...  ... ... ... ...   ← Human's responses
             ↓         ↓       ↓
           +10        -10       0   ← Terminal scores
```

Minimax **exhaustively explores every possible future** from the current board state. The AI (maximizer) picks moves that lead to the highest score; the human (minimizer) is assumed to respond with the lowest. The best move is guaranteed to be optimal.

| Property | Value |
|----------|-------|
| Strategy | Exhaustive game-tree search |
| Nodes on empty board | ~549,945 |
| Guaranteed optimal | ✅ Yes |
| Time on first move | ~150 ms |

---

### 02 · Alpha-Beta Pruning

```
           [Root]  α=-∞  β=+∞
           /              \
        [Left]            [Right]
        α=10               ← PRUNED ✂
        /    \              (can't improve
      +10    -5             over α=10)
```

Alpha-Beta is Minimax with **intelligence about which branches to skip**. It tracks:
- **α (alpha)** — best score the AI can guarantee
- **β (beta)** — best score the human can guarantee

When `α ≥ β`, the current branch is **pruned** — the opponent will never allow it, so exploring further is pointless. Same result. Dramatically fewer nodes.

| Property | Value |
|----------|-------|
| Strategy | Minimax + branch pruning |
| Nodes on empty board | ~30,709 |
| Guaranteed optimal | ✅ Yes (identical to Minimax) |
| Time on first move | <5 ms |

---

## ◈ Performance Results

```
┌─────────────────────────────────────────────────────────┐
│               FIRST MOVE — EMPTY BOARD                  │
├──────────────────┬──────────────────┬───────────────────┤
│   Algorithm      │   Nodes Visited  │   Time (approx.)  │
├──────────────────┼──────────────────┼───────────────────┤
│   Minimax        │      549,945     │     ~150 ms        │
│   Alpha-Beta     │       30,709     │      <5 ms         │
├──────────────────┼──────────────────┼───────────────────┤
│   REDUCTION      │       94.4%  ✂   │     97% faster     │
└──────────────────┴──────────────────┴───────────────────┘
```

> Alpha-Beta Pruning visited **94.4% fewer nodes** while producing the **exact same move** with **identical optimality guarantees**.

---

## ◈ Project Structure

```
TicTacToe_AI/
│
├── tictactoe.py          ← Main game file (all logic + AI)
│   ├── Section 1         Board representation
│   ├── Section 2         Move generation
│   ├── Section 3         Win / draw detection
│   ├── Section 4         Utility scoring function
│   ├── Section 5         Minimax algorithm
│   ├── Section 6         Alpha-Beta Pruning
│   ├── Section 7         Node count comparison
│   └── Section 8         Human vs AI game loop
│
├── report.md             ← Full analysis + MCTS / MDP comparison
└── README.md             ← You are here
```

---

## ◈ How to Run

**Prerequisites:** Python 3.x installed · No external libraries needed

```bash
# Clone or download the project
cd TicTacToe_AI

# Run the game
python tictactoe.py
```

**When prompted:**

```
Do you want to play as X (goes first) or O?
→ Enter: X  or  O

Which AI algorithm should play against you?
→ [1] Minimax only
→ [2] Alpha-Beta Pruning only
→ [3] Both — compare node counts every move  ← recommended
```

---

## ◈ Sample Game Output

```
  YOUR TURN ('X')
  Your move (enter a number 0-8): 4

   0 | 1 | 2
  ---+---+---
   3 | X | 5
  ---+---+---
   6 | 7 | 8

  AI is thinking... ('O')

  ══════════════════════════════════════════════════════
    ALGORITHM COMPARISON (same board state)
  ══════════════════════════════════════════════════════
    Algorithm              Nodes Visited    Time (ms)
    ──────────────────────────────────────────────────
    Minimax                      15,552        12.301
    Alpha-Beta                    1,248         0.821
    Alpha-Beta pruned 92.0% of nodes!
  ══════════════════════════════════════════════════════

  AI plays position 0
```

---

## ◈ Algorithm Comparison — Beyond Minimax

| Algorithm | Type | Optimal? | Handles Large Games? | Uncertainty? |
|-----------|------|:--------:|:-------------------:|:------------:|
| **Minimax** | Exhaustive search | ✅ | ❌ | ❌ |
| **Alpha-Beta** | Pruned search | ✅ | ⚠️ Better | ❌ |
| **MCTS** | Random simulation | ⚠️ Approx. | ✅ | ⚠️ |
| **MDP + Value Iter.** | Dynamic programming | ✅ | ❌ | ✅ |
| **Q-Learning (RL)** | Model-free learning | ⚠️ Approx. | ✅ | ✅ |

> Full analysis in [`report.md`](./report.md)

---

## ◈ Key Takeaways

```
  ① Minimax guarantees optimal play by searching the entire game tree.

  ② Alpha-Beta Pruning produces the same optimal result — 
     up to 94% faster by skipping irrelevant branches.

  ③ For small games like Tic-Tac-Toe, exhaustive search is feasible.
     For larger games (Chess, Go), heuristics + MCTS become necessary.

  ④ The AI is unbeatable — the best a human can achieve is a draw.
```

---

## ◈ Evaluation Criteria

| Component | Weight |
|-----------|:------:|
| Minimax implementation | 30% |
| Alpha-Beta Pruning | 30% |
| Human vs AI game | 25% |
| Code quality + Report | 15% |

---

<div align="center">

<br>

```
  ✕ ─────── ○ ─────── ✕
  │   Built with Python  │
  ○ ─────── ✕ ─────── ○
```

**Made for an AI Course Project**
*No libraries. No shortcuts. Just clean, readable Python.*

<br>

</div>
