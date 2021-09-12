import string


class Translator:
    """Перевод СС"""
    def __init__(self, number: str, from_base: str, to_base: str):
        """
        Ввод начальных данных для перевода
        :param number: число
        :param from_base: в какой оно сс
        :param to_base: в какой нужно сс
        """
        self.number = number
        self.from_base = from_base
        self.to_base = to_base

    def translator(self):
        """
        1)Переводим из str->int
        2)Проверяем на существование сс
        3)Сам перевод сс
        :return: возвращаем число
        """
        try:
            from_base = int(self.from_base)
            to_base = int(self.to_base)
            number = int(self.number, base=from_base)
        except ValueError:
            return '#Ошибка ввода!'
        else:
            alphabet = string.digits + string.ascii_uppercase
            if to_base > len(alphabet):
                return f'#Осн. не принадлежит [2:{len(alphabet)}]!'
            try:
                result = ""
                while number > 0:
                    number, mod = divmod(number, to_base)
                    result += alphabet[mod]
                return result[::-1]
            except ValueError:
                return '#Ошибка!'


class Calc:
    """Калькулятор СС"""
    def __init__(self, operand1: str, base1: str, operand2: str, base2: str, operation: str):
        """
        Ввод начальных данных
        :param operand1: первое число
        :param base1: первая сс
        :param operand2: второе число
        :param base2: вторая сс
        :param operation: знак операции
        """
        self.operand1 = operand1
        self.base1 = base1
        self.operand2 = operand2
        self.base2 = base2
        self.operation = operation

    def calc(self):
        """
        1)Все сс из str->int
        2)Перевод в 10 обоих чисел
        3)Операция
        :return: возврат числа
        """
        try:
            base1 = int(self.base1)
            base2 = int(self.base2)
            operand1_10 = int(self.operand1, base=base1)
            operand2_10 = int(self.operand2, base=base2)
        except ValueError:
            return '#Ошибка ввода!'
        else:
            try:
                if self.operation == '+':
                    return str(operand1_10 + operand2_10)
                if self.operation == '-':
                    return str(operand1_10 - operand2_10)
                if self.operation == '/':
                    return str(f"{(operand1_10 / operand2_10):.{1}f}")
                if self.operation == '*':
                    return str(operand1_10 * operand2_10)
                else:
                    return '#Данное действие не поддерживается!'
            except ZeroDivisionError:
                return '#Деление на ноль!'

