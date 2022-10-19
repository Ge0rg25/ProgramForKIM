import math
import eel

from .BASE import BaseFunctions


class Speed(BaseFunctions):
    def __init__(self):
        self.output = ""

    def return_speed(self, value1: str, value2: str):
        self.output = str((int(value1.strip().replace(" ", "")) / int(value2.strip().replace(" ", ""))))
        self.render(self.output)

    def register_speed(self):
        funcs = (
            self.return_speed,
        )
        for func in funcs:
            eel.expose(func)
