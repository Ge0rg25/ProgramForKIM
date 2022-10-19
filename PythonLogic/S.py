import math
import eel

from .BASE import BaseFunctions


class S(BaseFunctions):
    def __init__(self):
        self.output = ""

    def return_s(self, value1: str, value2: str):
        self.output = str((int(value1.strip().replace(" ", "")) * int(value2.strip().replace(" ", ""))))
        self.render(self.output)

    def register_s(self):
        funcs = (
            self.return_s,
        )
        for func in funcs:
            eel.expose(func)
