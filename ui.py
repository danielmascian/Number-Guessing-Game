from settings import DIFFICULTY_LEVELS


def show_welcome() -> None:
    print("Welcome to the Number Guessing Game!")
    print("Please select the difficulty level:")
    for level, (name, chances) in DIFFICULTY_LEVELS.items():
        print(f"{level}. {name} ({chances} chances)")


def prompt_difficulty() -> tuple[str, int]:
    while True:
        difficulty = input("Enter the difficulty level (1, 2, or 3): ").strip()
        if difficulty in DIFFICULTY_LEVELS:
            name, chances = DIFFICULTY_LEVELS[difficulty]
            print(f"You have selected {name} mode. You have {chances} chances to guess the number.")
            return name, chances
        print("Please choose 1, 2, or 3.")


def prompt_guess(min_number: int, max_number: int) -> int:
    while True:
        guess_text = input("Enter your guess: ").strip()
        if not guess_text.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess_text)
        if min_number <= guess <= max_number:
            return guess

        print(f"Please enter a number between {min_number} and {max_number}.")


def ask_play_again() -> bool:
    while True:
        answer = input("Do you want to play again? (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Please enter yes or no.")


def show_hint(guess: int, number_to_guess: int) -> None:
    if guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")


def show_win(number_to_guess: int, attempts: int) -> None:
    print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")


def show_loss(number_to_guess: int) -> None:
    print(f"Sorry, you've run out of chances. The number was {number_to_guess}.")


def show_goodbye() -> None:
    print("Thank you for playing! Goodbye.")
