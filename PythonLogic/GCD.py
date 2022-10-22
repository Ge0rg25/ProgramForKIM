import math
import eel

from .BASE import BaseFunctions


class Gcd(BaseFunctions):
    """
    Логика вычисления НОД
    """
    def __init__(self):
        self.output = ""

    def return_gcd(self, value1: str, value2: str):
        """
        Высчитывает НОД

        :param value1: Первое число
        :param value2: Второе число
        :return: None
        """
        self.output = str(math.gcd(int(value1.strip().replace(" ", "")), int(value2.strip().replace(" ", ""))))
        self.render(self.output)

    def register_gcd(self):
        """
        Регистрация методов подсчёта НОД

        :return: None
        """
        funcs = (
            self.return_gcd,
        )
        for func in funcs:
            eel.expose(func)
