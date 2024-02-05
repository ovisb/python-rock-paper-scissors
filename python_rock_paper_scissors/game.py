class Game:
    def __init__(self, available_choices: list[str]):
        self.__available_choices = available_choices

    @staticmethod
    def check_winner(choice: str, who_beats_choice: list[str]) -> bool:
        return choice in who_beats_choice

    def get_winner_list(self, choice: str) -> list[str]:
        choice_index = self.__available_choices.index(choice)
        choices = (
            self.__available_choices[choice_index + 1 :]
            + self.__available_choices[:choice_index]
        )

        winners_who_beat_choice = choices[: len(choices) // 2]

        return winners_who_beat_choice
