from CCcalc import Calc, Translator

if __name__ == '__main__':
    start1 = Calc('11', '2', '11', '2', '+')
    print(start1.calc())
    start2 = Translator('10', '2', '10')
    print(start2.translator())