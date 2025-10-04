"""Main module to run the Tic Tac Toe game"""

from game_processor import GameProcessor
from game_display import GameDisplay


if __name__ == "__main__":

    game_display = GameDisplay()
    game_processor = GameProcessor()
    board = game_display.generate_board()
    winning_patterns = game_display.setup_winning_patterns()
    current_player = 1
    for _ in range(9):
        game_display.display_final_board(board)
        game_processor.place_player_input(board, current_player)
        if game_processor.check_winner(board, winning_patterns):
            print(f"Player {current_player} wins!")
            break
        current_player = 2 if current_player == 1 else 1
    game_display.display_final_board(board)
