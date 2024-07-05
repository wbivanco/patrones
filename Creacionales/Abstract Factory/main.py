"""3. Aquí se define la clase principal que instancia los productos."""

from concrete_factory import DarkUIFactory, LightUIFactory

def client_code(factory):
    button = factory.create_button()
    textbox = factory.create_textbox()

    button.paint()
    textbox.paint()

if __name__ == "__main__":
    client_code(LightUIFactory())
    print()
    client_code(DarkUIFactory())