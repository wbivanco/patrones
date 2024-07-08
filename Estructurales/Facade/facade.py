"""4. Llamo a todos los subsistemas y verifico sus estados."""

from subsystem1 import Inventory
from subsystem2 import Payment
from subsystem3 import Shipping


class OnlineShoppingFacade:
    def __init__(self):
        self.inventory = Inventory()
        self.payment = Payment()
        self.shipping = Shipping()

    def place_order(self, user_id, product_id, amount):
        if self.inventory.check_inventory(product_id) and self.payment.process_payment(user_id, amount):
                return self.shipping.check_shipping(user_id, product_id)                
        else:
            return "Unable to place order"