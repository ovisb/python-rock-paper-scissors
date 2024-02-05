from file_handler import FileHandler
from game_interface import GameInterface


def main() -> None:
    file_handler = FileHandler("rating.txt")

    game = GameInterface(file_handler)
    game.start_game()


if __name__ == "__main__":
    main()
