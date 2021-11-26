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

    def update(self, data):
        """
        Выводит информацию снизу вверх:
            Сначала выводит поле интеракции с игроком (поле ввода текста или список действий для выбора),
            Отчеркивание,
            История вводимых команд и ответов игры.
            # оставляя место для кнопок

        Здесь же реализуются прочие визуальные и звуковые эффекты.

        data: новые данные и инструкции для отображения
        """  # тут же, если будет нужен, вывод состояния героя и или инвенторя

        pass  # FIXME
