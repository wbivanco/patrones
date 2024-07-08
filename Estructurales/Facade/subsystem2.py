"""2. Verifica si se pudo procesar el pago."""

class Payment:
    def process_payment(self, user_id, amount):
        print(f'Processing payment for user_id {user_id} amount {amount}')
        return True