import random

from file_handler import FileHandler
from game import Game


class GameInterface:
    def __init__(self, file_handler: "FileHandler"):
        self.__file_handler = file_handler
        self.__available_choices = ["rock", "paper", "scissors"]
        self.__player_name = None
        self.__initial_player_setup()
        self.__initial_choices_setup()
        self.__game = Game(self.__available_choices)

    def start_game(self) -> None:
        print("Okay, let's start")

        while True:
            user_choice = input()

            if user_choice == "!rating":
                rating = self.__check_rating(self.__player_name)
                print(f"Your rating: {rating}")
                continue

            if user_choice == "!exit":
                print("Bye!")
                break

            if user_choice not in self.__available_choices:
                print("Invalid input")
                continue

            computer_choice = random.choice(self.__available_choices)

            who_beats_user = self.__game.get_winner_list(user_choice)
            who_beats_comp = self.__game.get_winner_list(computer_choice)

            if self.__game.check_winner(computer_choice, who_beats_user):
                print(f"Sorry, but the computer chose {computer_choice}")
            elif self.__game.check_winner(user_choice, who_beats_comp):
                print(f"Well done. The computer chose {computer_choice} and failed")
                self.__add_score(100)
            else:
                print(f"There is a draw ({user_choice})")
                self.__add_score(50)

    def __add_score(self, score: int):
        names = self.__file_handler.load()
        names[self.__player_name] += score
        self.__file_handler.save(names)

    def __check_rating(self, name: str) -> int:
        names = self.__file_handler.load()

        return names[name]

    def __set_initial_score(self) -> None:
        names = self.__file_handler.load()
        if self.__player_name in names:
            return

        names.setdefault(self.__player_name, 0)
        self.__file_handler.save(names)

    def __initial_player_setup(self):
        self.__player_name = input("Enter your name: ")
        self.__set_initial_score()

        print(f"Hello, {self.__player_name}")

    def __initial_choices_setup(self):
        choices = input()
        if choices:
            self.__available_choices = choices.split(",")
