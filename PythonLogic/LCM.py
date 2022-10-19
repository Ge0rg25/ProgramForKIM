import math
import eel

from .BASE import BaseFunctions


class Lcm(BaseFunctions):
    def __init__(self):
        self.output = ""

    def return_lcm(self, value1: str, value2: str):
        self.output = str(math.lcm(int(value1.strip().replace(" ", "")), int(value2.strip().replace(" ", ""))))
        self.render(self.output)

    def register_lcm(self):
        funcs = (
            self.return_lcm,
        )
        for func in funcs:
            eel.expose(func)
