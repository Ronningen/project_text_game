"""
Главный модуль модели игры, содержащая мир, героя и все механики.
"""


class GameObject():
    """
    Базовый класс всех игровых объектов.
    """

    def __init__(self, description: str) -> None:
        self.description = description

    def descript(self) -> str:
        """
        Возвращает текстовое описание.
        """
        return self.description


class Location(GameObject):
    """
    Локация, в которой разворачиваются события, в которой игрок может находить предметы, загадки, врагов.
    """

    def __init__(self, description: str, objects) -> None:
        super().__init__(description)
        self.objects = objects


class Door(GameObject):
    """
    Основная дверь, просто связывает между собой две локации.
    """

    def __init__(self, description: str, enter_location: Location, aim_location: Location) -> None:
        super().__init__(description)
        self.enter_location = enter_location
        self.aim_location = aim_location


class World:  # FIXME
    """
    Основной класс игры, содержащий в себе текущую сцену, информацию о прогрессе игрока, героя и предметы.
    """

    def __init__(self) -> None:
        """
        Реализует игровое наполнение, вызывает создание персонажа и начинает тутуориал.
        """
        self.locations = []
        self.doors = []

        self.hero = []
        self.inventory = []
        
        self.current_location = None
        self.current_doors = []
        # FIXME

    def dispatch_command(command: str):
        """
        Отдает миру команду для какого-то действия.
        Принимает строку, пытается распознать в ней вызов какой-то заранее заданой команды и вызывает соответсвующий метод.
        Если команда не была распознана, должен вызывать сообщение о некоректности команды.
        Примеры предполагаемых команд: осмотреться, просмотреть свой инвентарь, ударить врага и т.д.
        Выполняет распознанную команду, изменяя соответсующие мир.
        - в качестве фичи можно преобразовывать ввод игрока во что-то стилизованное под запись в дневнике.

        returns: кортеж двух строк - (отформатированная команда, ответ игры на команду)
        """
        formated_command = ""  # запись введенной команды в нужном формате
        responce = ""  # ответ игры
        # FIXME
        return (formated_command, responce)
