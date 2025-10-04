"""Module containing classes for Tic Tac Toe game processing"""


class GameProcessor:

    """Process game logic for Tic Tac Toe"""
    def place_player_input(self, board, player):
        """Prompt the player for a move and update the board accordingly."""
        try:
            if player == 1:
                print("Player 1, Select your move (X):")
            else:
                print("Player 2, Select your move (O):")

            move = input("Enter your move (row,col): ")
            row, col = map(int, move.split(","))
            if board[row, col] == "*":
                if player == 1:
                    board[row, col] = "X"
                else:
                    board[row, col] = "O"
            else:
                print("Invalid move. Try again.")
                self.place_player_input(board, player)

        except (ValueError, IndexError):
            print("Invalid input format. Please enter row and column as 'row,col'.")
            self.place_player_input(board, player)

    def check_winner(self, board, winning_patterns):
        """Check the board for a winner based on the winning patterns."""
        for pattern in winning_patterns:
            if all(board[row, col] == "X" for row, col in pattern):
                return 1
            if all(board[row, col] == "O" for row, col in pattern):
                return 2
        return 0
