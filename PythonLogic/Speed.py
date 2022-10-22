import math
import eel

from .BASE import BaseFunctions


class Speed(BaseFunctions):
    """
    Логика вычисления скорости
    """

    def __init__(self):
        self.output = ""

    def return_speed(self, value1: str, value2: str):
        """
        Вычисляет скорость

        :param value1: Расстояние
        :param value2: Время
        :return: None
        """
        self.output = str((int(value1.strip().replace(" ", "")) / int(value2.strip().replace(" ", ""))))
        self.render(self.output)

    def register_speed(self):
        """
        Регистрация всех методов вычисления скорости

        :return: None
        """
        funcs = (
            self.return_speed,
        )
        for func in funcs:
            eel.expose(func)
