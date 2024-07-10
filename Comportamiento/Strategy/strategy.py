"""1. Define las interfaces de las implementaciones concretas y su clase abstracta."""


from abc import ABC, abstractmethod


class CommitionStrategy(ABC):
    @abstractmethod
    def calculate_commition(self, amount):
        pass


class FixedCommition(CommitionStrategy):
    def calculate_commition(self, amount):
        return 5    
    

class PercentageCommition(CommitionStrategy):
    def calculate_commition(self, amount):
        return amount * 0.05