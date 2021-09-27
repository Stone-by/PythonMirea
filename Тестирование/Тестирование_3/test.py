import unittest
from Res import Game_back


class UnitTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Game_back.hello('123!'), 'Я не знаю, что ты говоришь! Пиши понятнее!')

    def test_2(self):
        self.assertEqual(Game_back.name('Игорь'), 'Привет, Игорь!')

    def test_3(self):
        self.assertEqual(Game_back.questions_1('что думаешь насчет чертения?'), 'Рук нет - сказать не могу.')

    def test_4(self):
        self.assertEqual(Game_back.questions_2('Понедельник?'), 'В аду бы видал эти дни...')

    def test_5(self):
        self.assertEqual(Game_back.questions_3('dota 2?'), 'Обажаю! Особенно, когда она удаленна с меня.')
