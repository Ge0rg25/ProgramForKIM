import math
import eel

from .BASE import BaseFunctions


class Gcd(BaseFunctions):
    def __init__(self):
        self.output = ""

    def return_gcd(self, value1: str, value2: str):
        self.output = str(math.gcd(int(value1.strip().replace(" ", "")), int(value2.strip().replace(" ", ""))))
        self.render(self.output)

    def register_gcd(self):
        funcs = (
            self.return_gcd,
        )
        for func in funcs:
            eel.expose(func)
