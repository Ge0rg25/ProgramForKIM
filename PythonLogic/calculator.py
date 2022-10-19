import eel
from .BASE import BaseFunctions


class CalculatorLogic(BaseFunctions):
    def __init__(self):
        self.num1 = "0"
        self.num2 = ""
        self.char = ''
        self.output = f"{self.num1} {self.char} {self.num2}"
        self.result_char = ""
        self.chek_char = ""

    def udate_output(self):
        self.output = f"{self.num1} {self.char} {self.num2}"

    def on_load(self):
        self.udate_output()
        self.render(self.output)

    def clear_values(self):
        self.num1 = "0"
        self.num2 = ""
        self.char = ''
        self.output = f"{self.num1} {self.char} {self.num2}"
        self.result_char = ""
        self.chek_char = ""

    def add_num(self, num):
        if self.char == '':
            if self.num1[0] == '0':
                self.num1 = ''
            self.num1 = self.num1 + str(num)
        else:
            self.num2 = self.num2 + str(num)
        self.udate_output()
        self.render(self.output)

    def add_char(self, char):
        self.char = char
        if char == "÷":
            self.chek_char = "/"
        elif char == "×":
            self.chek_char = "*"
        else:
            self.chek_char = char
        self.udate_output()
        self.render(self.output)

    def return_result(self):
        first_num = int(self.num1)
        second_num = int(self.num2)
        if self.chek_char == "+":
            self.result_char = str(first_num + second_num)
        elif self.chek_char == "-":
            self.result_char = str(first_num - second_num)
        elif self.chek_char == "/":
            self.result_char = str(int(first_num / second_num))
        elif self.chek_char == "*":
            self.result_char = str(first_num * second_num)
        self.render(self.result_char)
        self.clear_values()

    def ce(self):
        self.clear_values()
        self.udate_output()
        self.render(self.output)

    def register_calculator_funcs(self):
        funcs = (
            self.add_num,
            self.add_char,
            self.on_load,
            self.return_result,
            self.ce,
        )
        for func in funcs:
            eel.expose(func)
