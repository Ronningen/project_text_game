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


class World():
    """
    Основной класс игры, содержащий в себе текущую сцену, информацию о прогрессе игрока, героя и предметы.
    """

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

    def dispatch_command(self, command: str): 
        #FIXME FIXME FIXME FIXME FIXME
        """
        Отдает миру команду для какого-то действия.
        Принимает строку, пытается распознать в ней вызов какой-то заранее заданой команды и вызывает соответсвующий метод.
        Если команда не была распознана, должен вызывать сообщение о некоректности команды.
        Примеры предполагаемых команд: осмотреться, просмотреть свой инвентарь, ударить врага и т.д.
        Выполняет распознанную команду, изменяя соответсующие мир.
        - в качестве фичи можно преобразовывать ввод игрока во что-то стилизованное под запись в дневнике.
        """

        def check_one(*keys):
            for key in keys:
                if key in command.lower():
                    return True
            return False

        def check_all(*keys):
            flag = True
            for key in keys:
                flag *= key in command.lower()
            return flag

        def run():
            self.response += "Мне удалось убежать."

        def fight():
            self.formatted_command += "Я решил сражаться."
            self.response += "Из-за угла вылетел кабан."
            self.command_list = [self.create_command(hit, "Удар!")]

        def hit():
            return "Победа! Кабан убежал!"

        if (check_one("карман") and check_one("рыск", "осмотр", "пошар")) or check_one("инвентарь"):
            self.formatted_command += "Порыскал по карманам."
            if len(self.inventory) > 0:
                items = list(map(lambda i: i.get_marker(), self.inventory))
                items_set = set(items)
                for i in items_set:
                    i += " x" + str(items.count(i))
                self.response += "Нашел " + ", ".join(items_set) + "."
            else:
                self.response += "Пусто..."

        elif check_one("осмотр"):
            self.formatted_command += "Я решил осмотреться."
            self.response += self.current_location.get_description()

        elif check_one("аааааааа"):
            self.formatted_command += "Я закричал от отчаяния."
            self.response += "К сожалению, крик услышали не только стены: я слышу чьи-то быстрые шаги - оно приближается."
            self.command_list = [Command(run, "убежать."),
                            Command(fight, "готовиться к битве."),]

        elif check_one("взя", "подн", "схват", "бра"):
            self.formatted_command += "Я решил подобрать "
            objects = self.current_location.objects
            picked_object = ""
            for object in objects:
                marker = object.get_marker()
                if check_one(marker):
                    marked_objects = []
                    for marked_object in objects:
                        if marked_object.get_marker() == marker:
                            marked_objects.append(marked_object)
                    if len(marked_objects) > 1:
                        for marked_object in objects:
                            if check_one(marked_object.get_place()):
                                picked_object = marked_object
                                break
                        if picked_object != "":
                            break
                        self.formatted_command += marker + ","
                        self.response += "но не определился конкретно. Надо тщательнее выбрать."
                    else:
                        picked_object = object
            if picked_object != "":
                self.formatted_command += picked_object.get_description() + "."
                self.response += "Буду носить его с собой."
                self.inventory.append(picked_object.delocate())
                self.current_location.objects.remove(picked_object)
            else:
                self.formatted_command += "что-то, "
                self.response += "но еще не решил что именно."
            

        else:
            self.response += """Опять заболела голова. Кажется, я слышу какие-то голоса... 
            Ничего не понимаю. Надо взять себя в руки."""
            
            
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

    def get_command_list(self):
        """
        Отдает список команд, при этом уничтожая его копию у себя.
        """
        command_list = self.command_list
        self.command_list = []
        return command_list

    def __init__(self) -> None:
        """
        Реализует игровое наполнение, вызывает создание персонажа и начинает тутуориал.
        """
        self.response = """
        Сколько времени я здесь?
        Голова болит.
        И все остальное...
        Надо попробовать открыть глаза.
        """  # ответ для записи в историю

        def open_eyes():
            self.formatted_command += """Это потребовало усилий, но у меня получилось."""
            self.response += """(Введите "осмотреться")"""

        self.formatted_command = ""  # форматированная команда для записи с историю
        self.command_list = [Command(open_eyes, "Открыть глаза.")]

        self.locations = [Location("Темная комната. Трудно понять, как давно тут кто-то был: слои пыли уже вековы, однако все кажется подозрительно живым", [
                                        LocatedObject("почему-то знакомый дневник", "дневник", "на полу"),
                                        LocatedObject("странная картина", "картин", "на стене"),
                                        LocatedObject("какой-то ржавый бесполезный меч", "меч", "в углу"),
                                        LocatedObject("Короткий меч", "меч", "на стене")
                        ])]
        self.current_location = self.locations[0]

        self.inventory = []



class GameObject():
    """
    Базовый класс всех игровых объектов.
    """

    def __init__(self, description: str, marker: str  = "") -> None:
        """
        marker - имя объекта, по которому к нему нужно обращаться в игре.
        description - подробное описание объекта, в нем объект должен называться только как marker.
        """
        self.description = description
        self.marker = marker

    def get_marker(self) -> str: 
        return self.marker

    def get_description(self) -> str:
        return self.description


class LocatedObject(GameObject):
    """
    Объект в локации. Дополнительно хранит свое положение на локации.
    """

    def __init__(self, description: str, marker: str, place: str = "") -> None:
        super().__init__(description, marker)
        self.place = place

    def get_place(self):
        return self.place

    def delocate(self):
        return super()


class Location(GameObject):
    """
    Локация, в которой разворачиваются события, в которой игрок может находить предметы, загадки, врагов.
    """

    def __init__(self, description: str, objects = []) -> None:
        super().__init__(description)
        self.objects = objects

    def get_description(self) -> str:
        full_description = super().get_description()
        if len(self.objects) > 0:
            full_description += " В ней есть: "
            for o in self.objects:
                full_description += o.get_description().lower() + " " + o.get_place().lower() + ", "
            full_description += "да и все."
        return full_description


class Bridge(GameObject):
    """
    Переход между двумя локациями.
    """

    def __init__(self, description: str, enter_location: Location, aim_location: Location) -> None:
        super().__init__(description)
        self.enter_location = enter_location
        self.aim_location = aim_location
