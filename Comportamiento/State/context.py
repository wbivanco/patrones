"""2. Define clase de una instancia de state y refleja el estado actual."""


from state import StopState


class MusicPlayer():
    def __init__(self):
        self.state = StopState()

    def press_play(self):
        self.state.press_play(self)