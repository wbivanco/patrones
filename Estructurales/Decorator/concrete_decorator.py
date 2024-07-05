"""4. Añade responsabilidades a los componentes concretos."""

from decorator import TextDecorator


class HTMLDecorator(TextDecorator):
    def render(self):
        return f'<html>{self._text_component.render()}</html>'