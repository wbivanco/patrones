"""2. Es la clase que se encarga de hacer el procesamiento de las estrategias."""


class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):    
        return self.strategy.calculate_commition(amount)