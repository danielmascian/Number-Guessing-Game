import random

from settings import MAX_NUMBER, MIN_NUMBER
from ui import prompt_difficulty, prompt_guess, show_hint, show_loss, show_welcome, show_win


def play_round() -> None:
    show_welcome()
    _, chances = prompt_difficulty()
    number_to_guess = random.randint(MIN_NUMBER, MAX_NUMBER)

    print(f"I have selected a number between {MIN_NUMBER} and {MAX_NUMBER}. Try to guess it!")

    for attempt in range(1, chances + 1):
        guess = prompt_guess(MIN_NUMBER, MAX_NUMBER)
        if guess == number_to_guess:
            show_win(number_to_guess, attempt)
            return
        show_hint(guess, number_to_guess)

    show_loss(number_to_guess)
