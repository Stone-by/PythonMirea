class RailingCalc:
    """Расчитывает конфигурацию перил в зависимости от параметров"""
    def __init__(self, baluster_width: float, distance_balusters: float):
        """
        Ввод начальных данных для расчета расположения балясин

        :param baluster_width: ширина балясины
        :param distance_balusters: расстояние между балясин
        """

        self.baluster_width = baluster_width
        self.balusters_distance = distance_balusters

    def get_baluster_positions(self, length: float) -> list[float]:
        """
        Вычисляет расстановку балясин в зависимости от длины пролета перил. Возможны две расстановки:
        1) центр одной из балясин совпадает с центром пролета
        2) центр пролета перил совпадает с серединой промежутка между центральными балясинами

        :param length: длина пролета перил
        :return: список отступов от начала пролета до края балясины
        """

        moved = [e - self.baluster_width / 2 for e in self._calculate(self._moved(length), length)]
        center = [e - self.baluster_width / 2 for e in self._calculate(length / 2, length)]

        return [] if not moved else center if moved[0] < self.balusters_distance / 2 else moved

    def _moved(self, length: float) -> float:
        """Возвращает начальную позицию смещенной балясины в зависимости от длины пролета"""
        return (length - self.balusters_distance - self.baluster_width) / 2

    def _calculate(self, current: float, length: float) -> list[float]:
        """
        Вычисляет расположение балясин в зависимости от длины пролета и начальной позиции

        :param current: начальная позиция
        :param length: длина пролета
        :return: список координат центров балясин
        """
        left = []
        while current > 0:
            left.append(round(current, 2))
            current -= self.balusters_distance + self.baluster_width
        left.reverse()
        try:
            current = left[-1] + self.balusters_distance + self.baluster_width
        except IndexError:
            return []
        while current < length:
            left.append(current)
            current += self.balusters_distance + self.baluster_width

        return left
