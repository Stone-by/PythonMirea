# Спецификация классов Calc и Translator
Классы Calc и Translator позволяют считать в разных СС и переводить из одной СС в другую соответственно в зависимости от нескольких параметров Calc • Первое число • Первое СС • Второе число • Второе СС • Действие; Translator • Число • Старая СС • Новая СС

Пример данных для ввода (operand1 '123', base1 '10', operand2 'AF23', base2 '16', operation '+') Пример неверных данных для ввода (operand1 '123.3', base1 '999', operand2 AF23, base2 '-23.2', operation +) Исключительно str в int виде для чисел(кроме ABCDEF для 16-38 СС), str в int от 2-38 для СС и str(+, -, , ) для операции

class Calc(builtins.object)  Возвращает результат действия с числами в 10ой СС  Calc(operand1 str, base1 str, operand2 str, base2 str, operation str) 
 Калькулятор СС 
 Methods defined here 
 init(self, operand1 str, base1 str, operand2 str, base2 str, operation str)  Ввод начальных данных  param operand1 первое число  param base1 первая сс  param operand2 второе число  param base2 вторая сс  param operation знак операции 
 calc(self)  1)Все сс из str-int  2)Перевод в 10 обоих чисел  3)Операция  return возврат число, либо ошибку 
 ----------------------------------------------------------------------

Пример данных для ввода (number '11', from_base '2', to_base '10') Пример неверных данных для ввода (number AF2, from_base '999', to_base '10.2') Исключительно str в неотрицательном int виде для чисел и str в int от 2-38 для двух СС

class Translator(builtins.object)  Возвращает перевод числа из одной СС в другую  Translator(number str, from_base str, to_base str) 
 Перевод СС 
 Methods defined here 
 init(self, number str, from_base str, to_base str)  Ввод начальных данных для перевода  param number число  param from_base в какой оно сс  param to_base в какой нужно сс 
 translator(self)  1)Переводим из str-int  2)Проверяем на существование сс  3)Сам перевод сс  return возврат число, либо ошибку 
 ----------------------------------------------------------------------
