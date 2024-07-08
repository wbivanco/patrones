"""5. Implemento la lógica de la fachada."""

from facade import OnlineShoppingFacade

facade = OnlineShoppingFacade()

print(facade.place_order("usuario", "producto", 10))