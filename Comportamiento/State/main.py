"""3. Implementa la lógica del ejemplo."""


from state import PlayingState, PausedState, StopState
from context import MusicPlayer


def main():
    player = MusicPlayer()

    player.press_play()
    player.press_play()
    player.press_play()

if __name__ == "__main__":
    main()