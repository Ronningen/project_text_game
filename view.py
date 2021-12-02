""" 
Интерфейс с пользователем, выводящий данные, полученные от ядра, и передает ему команды пользователя.
"""
import pygame

FONT = pygame.font.SysFont("Arial", 20)


class WindowElement:
    def __init__(self, screen, rect: pygame.Rect) -> None:
        self.screen = screen
        self.rect = pygame.Rect(rect)
        self.focused = False

    def focus(self, pos):
        self.focused = self.rect.collidepoint(pos)

    def show():
        pass


class Button(WindowElement):
    """
    Экранная кнопка, выполняющая заданное ей действие
    """

    def __init__(self, screen, rect: pygame.Rect, action, text=""):
        super().__init__(screen, rect)
        self.action = action
        self.text = text

    def show(self):
        """
        В пределах rect кнопки рисует ее в зависимимости от того, наведена ли мышь на кнопку или нет - focused
        """
        pygame.draw.rect(self.screen, (100, 100, 100), self.rect)  # FIXME

    def call_action(self):
        """
        Совершает заложенное действие, если кнопка в фокусе. Предпалагается использоваться по нажатию мыши
        """
        if self.focused:
            self.action()


class GameView:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        # FIXME - продумать необходимые для работы поля

    def add_command(self, text: str):
        """
        Добовнляет новый абазац c текстом команды игрока в историю.
        Метод работает только с полями класса, ничего не отрисовывает.
        """
        pass # FIXME

    def add_responce(self, text: str):
        """
        Добовнляет новый абазац с текстом ответы игры в историю.
        Метод работает только с полями класса, ничего не отрисовывает.
        """
        pass # FIXME

    def update(self):
        """
        Выводит информацию СНИЗУ-ВВЕРХ:  оставляя место для кнопок
            Сначала выводит поле интеракции с игроком (поле ввода текста или список действий для выбора),
            Отчеркивание,
            История вводимых команд и ответов игры.
            
        Элементы истории, ушедшие за границы экрана должны удаляться из памяти.

        Здесь же реализуются прочие визуальные и звуковые эффекты.
        """  # тут же, если будет нужен, вывод состояния героя и или инвенторя

        pass  # FIXME
