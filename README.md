# 🎮 Tic-Tac-Toe AI: Minimax vs. Alpha-Beta Pruning

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python)
![AI Approach](https://img.shields.io/badge/AI-Adversarial%20Search-darkgreen?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-red?style=for-the-badge)

A highly optimized, educational command-line Tic-Tac-Toe game built with Python. This project implements adversarial search tree concepts using **Classic Minimax** and optimized **Alpha-Beta Pruning**, demonstrating how mathematical pruning techniques can drastically reduce algorithmic complexity without compromising decision quality.

---

## 🎯 Key Takeaways

* 🧠 **Adversarial Logic**: The AI acts as a *maximizer* to secure the highest utility score, while anticipating the human opponent acting as a *minimizer*.
* ✂️ **Alpha-Beta Optimization**: Speeds up tree evaluations by skipping irrelevant branches as soon as a worse option is proven.
* 📈 **Scale Limitations**: Small game spaces like Tic-Tac-Toe can be exhaustively searched to terminal states. Large games (e.g., Chess, Go) require strict depth limits and custom heuristic evaluation functions.

---

## ✨ Features

- **Robust Game Engine**: Built-in dynamic board rendering, legal move verification, and accurate win/draw validation.
- **Dual Algorithmic Modes**: Play against an unpruned standard Minimax algorithm or an optimized Alpha-Beta Pruning engine.
- **Real-Time Telemetry**: Track and display the **total node count evaluated** after every move to directly observe algorithmic efficiency.
- **Detailed Theoretical Review**: Comparative evaluation of alternative tree-search methodologies like MCTS and MDP.

---

## 🚀 Step-by-Step Guide for VS Code (Beginner Friendly)

Follow these direct steps to set up, edit, and run this project inside **Visual Studio Code**:

### Step 1: Install Python
Ensure Python is installed on your computer. You can download it from [python.org](https://www.python.org/).

### Step 2: Set Up Your Extensions in VS Code
1. Open **VS Code**.
2. Click on the **Extensions icon** on the left-side activity bar (looks like 4 blocks).
3. Search for **"Python"** (by Microsoft) and click **Install**.

### Step 3: Create the Game File
1. Click **File > New File...** or press `Ctrl + N` (`Cmd + N` on Mac).
2. Save the file immediately as `tictactoe_ai.py` via **File > Save As...**.
3. Copy and paste the core script code into this file.

### Step 4: Run the Application
1. Click the **Run Button** (the small triangle play icon in the top right corner of VS Code).
2. Alternatively, open the terminal inside VS Code (`Ctrl + ~`) and execute:
