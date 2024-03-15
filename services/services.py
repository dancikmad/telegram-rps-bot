import random

from lexicon.lexicon_en import LEXICON_EN


def get_bot_choice() -> str:
    """Function returns random choice for Bot in the game"""
    return random.choice(["rock", "paper", "scissors"])


def __normalize_user_answer(user_answer: str) -> str:
    """
    Returns the key from the dictionary corresponding to the provided value.
    """
    for key in LEXICON_EN:
        if LEXICON_EN[key] == user_answer:
            break

    return key


def get_winner(user_choice: str, bot_choice: str) -> str:
    """Function determins the winner of the game based on user and bot choices."""
    user_choice = __normalize_user_answer(user_choice)
    rules = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    if user_choice == bot_choice:
        return "nobody_won"
    elif rules[user_choice] == bot_choice:
        return "user_won"
    return "bot_won"
