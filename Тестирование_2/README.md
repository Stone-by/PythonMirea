# Спецификация классов Calc и Translator
Классы Calc и Translator позволяют считать в разных СС и переводить из одной СС в другую соответственно в зависимости от нескольких параметров: Calc: • Первое число • Первое СС • Второе число • Второе СС • Действие; Translator: • Число • Старая СС • Новая СС  

class Calc(builtins.object)
 |  Calc(operand1: str, base1: str, operand2: str, base2: str, operation: str)
 |  
 |  Калькулятор СС
 |  
 |  Methods defined here:
 |  
 |  __init__(self, operand1: str, base1: str, operand2: str, base2: str, operation: str)
 |      Ввод начальных данных
 |      :param operand1: первое число
 |      :param base1: первая сс
 |      :param operand2: второе число
 |      :param base2: вторая сс
 |      :param operation: знак операции
 |  
 |  calc(self)
 |      1)Все сс из str->int
 |      2)Перевод в 10 обоих чисел
 |      3)Операция
 |      :return: возврат числа
 |  
 |  ----------------------------------------------------------------------

class Translator(builtins.object)
 |  Translator(number: str, from_base: str, to_base: str)
 |  
 |  Перевод СС
 |  
 |  Methods defined here:
 |  
 |  __init__(self, number: str, from_base: str, to_base: str)
 |      Ввод начальных данных для перевода
 |      :param number: число
 |      :param from_base: в какой оно сс
 |      :param to_base: в какой нужно сс
 |  
 |  translator(self)
 |      1)Переводим из str->int
 |      2)Проверяем на существование сс
 |      3)Сам перевод сс
 |      :return: возвращаем число
 |  
 |  ----------------------------------------------------------------------
