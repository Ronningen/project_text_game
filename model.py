"""
Главный модуль модели игры, содержащая мир, героя и все механики.
"""

class Command():
    """
    Инкапсуляция функции и ее названия.
    """
    def __init__(self, func, name) -> None:
        self.func = func
        self.name = name

    def get_func(self):
        return self.func

    def get_name(self):
        return self.name

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


class Bridge(GameObject):
    """
    Переход между двумя локациями.
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
        self.response = "" #ответ для записи в историю
        self.formatted_command = "" #форматированная команда для записи с историю

        self.locations = []
        self.doors = []

        self.hero = []
        self.inventory = []

        self.current_location = None
        self.current_doors = []
        # FIXME

    
    def get_response(self):
        """
        Отдает ответ, при этом уничтожая его копию у себя.
        """
        response = self.response
        self.response = ""
        return response

    def get_command(self):
        """
        Отдает текст команды, при этом уничтожая его копию у себя.
        """
        formatted_command = self.formatted_command
        self.formatted_command = ""
        return formatted_command

    def dispatch_command(self, command: str):
        """
        Отдает миру команду для какого-то действия.
        Принимает строку, пытается распознать в ней вызов какой-то заранее заданой команды и вызывает соответсвующий метод.
        Если команда не была распознана, должен вызывать сообщение о некоректности команды.
        Примеры предполагаемых команд: осмотреться, просмотреть свой инвентарь, ударить врага и т.д.
        Выполняет распознанную команду, изменяя соответсующие мир.
        - в качестве фичи можно преобразовывать ввод игрока во что-то стилизованное под запись в дневнике.

        returns: список дальнейших команд.
        Если дальнейшая команда произвольна и должна быть введена с клавиатуры, то список команд пуст.
        """

        self.formatted_command += command  # запись введенной команды в нужном формате
        self.response += "Хорошая работа! Теперь нажмите на любую из кнопок - они одинаковы"  # ответ игры
        command_list = [self.create_command(lambda: '', "первое ничего"),
                        self.create_command(lambda: '', "второе ничего"),
                        self.create_command(lambda: '', "третье ничего")]
        # FIXME
        return command_list

    def create_command(self, func, name):
        """
        Инкапсулирует функцию и ее название.
        При этом изменяет функцию так, что ее результат записывается в поле self.message этого World.
        Забрать из этого World поле self.message можно с помощью метода get_messege().
        """
        def func_with_responce():
            self.formatted_command += name
            self.response += str(func())
        return Command(func_with_responce, name)
