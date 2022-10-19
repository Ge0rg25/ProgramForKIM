import math
import eel

from .BASE import BaseFunctions


class Distance(BaseFunctions):
    def __init__(self):
        self.output = ""

    def return_distance(self, value1: str, value2: str):
        self.output = str((int(value1.strip().replace(" ", "")) * int(value2.strip().replace(" ", ""))))
        self.render(self.output)

    def register_distance(self):
        funcs = (
            self.return_distance,
        )
        for func in funcs:
            eel.expose(func)
