import pytest

from python_rock_paper_scissors.game import Game


@pytest.fixture
def default_constructor():
    game = Game(["rock", "paper", "scissors"])
    return game


@pytest.fixture
def test_winner_list(default_constructor):
    user_choice = "rock"
    return default_constructor.get_winner_list(user_choice)


def test_winner(default_constructor, test_winner_list):
    computer_choice = "paper"
    assert default_constructor.check_winner(computer_choice, test_winner_list) is True
