"""3. Maneja y ejecuta comandos."""


class Button:
    def __init__(self, command):
        self.command = command # Puede ir diccionario de comandos

    def press(self):
        self.command.execute()