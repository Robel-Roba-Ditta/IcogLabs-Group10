import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.human = 'O'
        self.ai = 'X'
        self.nodes_evaluated = 0

    def print_board(self):
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("---+---+---")
        print()

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def check_win(self, player):
        win_lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], 
            [0, 3, 6], [1, 4, 7], [2, 5, 8], 
            [0, 4, 8], [2, 4, 6]             
        ]
        for line in win_lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] == player:
                return True
        return False

    def is_draw(self):
        return ' ' not in self.board

    def minimax(self, is_maximizing):
        self.nodes_evaluated += 1

        if self.check_win(self.ai): return 1
        if self.check_win(self.human): return -1
        if self.is_draw(): return 0

        if is_maximizing:
            best_score = -math.inf
            for move in self.available_moves():
                self.board[move] = self.ai
                score = self.minimax(False)
                self.board[move] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for move in self.available_moves():
                self.board[move] = self.human
                score = self.minimax(True)
                self.board[move] = ' '
                best_score = min(score, best_score)
            return best_score

    def alpha_beta(self, is_maximizing, alpha, beta):
        self.nodes_evaluated += 1

        if self.check_win(self.ai): return 1
        if self.check_win(self.human): return -1
        if self.is_draw(): return 0

        if is_maximizing:
            best_score = -math.inf
            for move in self.available_moves():
                self.board[move] = self.ai
                score = self.alpha_beta(False, alpha, beta)
                self.board[move] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = math.inf
            for move in self.available_moves():
                self.board[move] = self.human
                score = self.alpha_beta(True, alpha, beta)
                self.board[move] = ' '
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return best_score

    def get_best_move(self, use_pruning=True):
        self.nodes_evaluated = 0
        best_score = -math.inf
        best_move = None

        for move in self.available_moves():
            self.board[move] = self.ai
            
            if use_pruning:
                score = self.alpha_beta(False, -math.inf, math.inf)
            else:
                score = self.minimax(False)
                
            self.board[move] = ' '

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

def play_game():
    game = TicTacToe()
    
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O'. Positions are 0-8 from top-left to bottom-right.\n")
    
    choice = input("Use Alpha-Beta Pruning? (y/n): ").strip().lower()
    use_pruning = True if choice == 'y' else False

    game.print_board()

    while True:
        # Human Move Loop
        valid_move = False
        while not valid_move:
            try:
                move = int(input("Enter your move (0-8): "))
                if move in game.available_moves():
                    game.board[move] = game.human
                    valid_move = True
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a number between 0 and 8.")

        game.print_board()
        if game.check_win(game.human):
            print("You win!")
            break
        if game.is_draw():
            print("It's a draw!")
            break

        # AI Move Loop
        print("AI is thinking...")
        best_move = game.get_best_move(use_pruning=use_pruning)
        game.board[best_move] = game.ai
        
        print(f"AI chose position {best_move}")
        print(f"Algorithm evaluated {game.nodes_evaluated} nodes.")
        game.print_board()

        if game.check_win(game.ai):
            print("AI wins!")
            break
        if game.is_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
