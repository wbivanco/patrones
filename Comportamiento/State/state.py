"""1. Define una clase abstracta del estado y los estados concretos."""


from abc import ABC, abstractmethod


class PlayerState(ABC):
    @abstractmethod
    def press_play(self, player):
        pass


class PlayingState(PlayerState):
    def press_play(self, player):
        print("Pausing")
        player.state = PausedState()


class PausedState(PlayerState):
    def press_play(self, player):
        print("Playing")
        player.state = PlayingState()


class StopState(PlayerState):
    def press_play(self, player):
        print("Playing")
        player.state = PlayingState()