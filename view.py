""" 
Интерфейс с пользователем, выводящий данные, полученные от ядра, и передает ему команды пользователя.
"""
import pygame

FONT = pygame.font.SysFont("Arial", 20)
textlines_number = 8
text_screen_portion = .8


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
    Экранная кнопка, выполняющая заданное ей действие.
    """

    def __init__(self, screen, rect: pygame.Rect, action, text=""):
        super().__init__(screen, rect)
        self.action = action
        self.text = text

    def show(self):
        """
        В пределах rect кнопки рисует ее в зависимимости от того, наведена ли мышь на кнопку или нет - focused.
        """
        if self.focused:
            pygame.draw.rect(self.screen, (100, 100, 100), self.rect)  # FIXME
            text_surface = FONT.render(self.text, 1, (255,255,255))
        else:
            pygame.draw.rect(self.screen, (30, 30, 30), self.rect)
            text_surface = FONT.render(self.text, 1, (80,80,80))
        text_rect = text_surface.get_rect(center = self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def call_action(self):
        """
        Совершает заложенное действие, если кнопка в фокусе. Предпалагается использоваться по нажатию мыши.
        """
        if self.focused:
            self.action()


class GameView:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.textlines = ["Привет! Введите любой текст и нажмите ENTER"]
#пара рандомных текстовых полей для теста
        # FIXME - продумать необходимые для работы поля
        # разобраться с колвом текста
    def add_command(self, command_text: str):
        """
        Добовнляет новый абазац c текстом команды игрока в историю.
        Метод работает только с полями класса, ничего не отрисовывает.
        """
        self.textlines.append(command_text)
        if len(self.textlines) > textlines_number:
            self.textlines.pop(0)
        # FIXME
    def add_response(self, response_text: str):
        """
        Добовнляет новый абазац с текстом ответы игры в историю.
        Метод работает только с полями класса, ничего не отрисовывает.
        """
        self.textlines.append(response_text)
        if len(self.textlines) > textlines_number:
            self.textlines.pop(0)
        # FIXME

    def update(self):
        w = self.screen.get_width()
        h = self.screen.get_height()
        textline_width = w
        textline_height = h * text_screen_portion/textlines_number
        """
        Выводит информацию СНИЗУ-ВВЕРХ:  оставляя место для кнопок
            Сначала выводит поле интеракции с игроком (поле ввода текста или список действий для выбора),
            Отчеркивание,
            История вводимых команд и ответов игры.

        Элементы истории, ушедшие за границы экрана должны удаляться из памяти.

        Здесь же реализуются прочие визуальные и звуковые эффекты.
        """  # тут же, если будет нужен, вывод состояния героя и или инвенторя
        for i in range(len(self.textlines)):
            textline_surface = FONT.render(self.textlines[-i-1], 1, (255,255,255))
            a = (0, textline_height*(textlines_number - i))
            textline_rect = textline_surface.get_rect(topleft = a)
            self.screen.blit(textline_surface, textline_rect)
#        render buttons
#        render imput window
#        FIXME

