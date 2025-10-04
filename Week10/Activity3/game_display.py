"""Module containing classes for Tic Tac Toe game display"""

import numpy as np


class GameDisplay:
    """Handle game display for Tic Tac Toe"""

    def display_final_board(self, board):
        """Display the final state of the game board."""
        for row in board:
            print(" | ".join(str(x) for x in row))
            # print("-" * 9)

    def generate_board(self):
        """Generate the initial game board."""
        return np.full((3, 3), "*")

    def setup_winning_patterns(self):
        """Set up and return the winning patterns."""
        return [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]
