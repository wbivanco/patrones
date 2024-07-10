"""3. Implementa la lógica del ejemplo."""


from strategy import FixedCommition, PercentageCommition
from context import PaymentProcessor

def main():    
    processor = PaymentProcessor(PercentageCommition())
    print(processor.process_payment(100))

    processor = PaymentProcessor(FixedCommition())
    print(processor.process_payment(100))

if __name__ == "__main__":  
    main()