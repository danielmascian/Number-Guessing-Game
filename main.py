from game import play_round
from ui import ask_play_again, show_goodbye


def main() -> None:
    while True:
        play_round()
        if not ask_play_again():
            show_goodbye()
            break

if __name__ == "__main__":
    main()