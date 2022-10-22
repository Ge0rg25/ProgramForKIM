import math
import eel

from .BASE import BaseFunctions


class S(BaseFunctions):
    """
    Логика вычисления площади
    """
    def __init__(self):
        self.output = ""

    def return_s(self, value1: str, value2: str):
        """
        Вычисляет площадь

        :param value1: Первая сторона
        :param value2: Вторая сторона
        :return: None
        """
        self.output = str((int(value1.strip().replace(" ", "")) * int(value2.strip().replace(" ", ""))))
        self.render(self.output)

    def register_s(self):
        """
        Регистрация методов вычисления площади

        :return: None
        """
        funcs = (
            self.return_s,
        )
        for func in funcs:
            eel.expose(func)
