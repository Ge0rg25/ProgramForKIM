import math
import eel

from .BASE import BaseFunctions


class P(BaseFunctions):
    def __init__(self):
        self.output = ""

    def return_p(self, value1: str, value2: str):
        self.output = str(((int(value1.strip().replace(" ", "")) + int(value2.strip().replace(" ", ""))) * 2))
        self.render(self.output)

    def register_p(self):
        funcs = (
            self.return_p,
        )
        for func in funcs:
            eel.expose(func)
