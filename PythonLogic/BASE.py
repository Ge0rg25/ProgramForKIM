import eel


class BaseFunctions:
    """
    Базовый функционал который должен быть в каждом классе
    """

    def render(self, output):
        eel.render_output(output)
