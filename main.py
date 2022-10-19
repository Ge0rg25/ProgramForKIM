import eel
from PythonLogic import CalculatorLogic, Gcd, Lcm, P, S, Distance, Speed


def run():
    eel.init("./WebInterface")
    CalculatorLogic().register_calculator_funcs()
    Gcd().register_gcd()
    Lcm().register_lcm()
    P().register_p()
    S().register_s()
    Distance().register_distance()
    Speed().register_speed()
    eel.start("index.html", size=(370, 640))


run()
