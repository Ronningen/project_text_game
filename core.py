"""
Главный модуль, содержит и управляет окнами приложения.
Среди окон есть меню и главное окно игры, связывающее игровую модель с интерфейсом.
"""
import pygame
pygame.init()

import view
import model
import data


WIDTH, HEIGHT = 400, 400


class Window:
    """
    Базовый класс, управляющий активным окном pygame
    Содержит и отображает экземпляры view.WindowElement - список controls
    """

    def __init__(self, screen, clock) -> None:
        self.screen = screen
        self.clock = clock
        self.controls = []

    def handle(self, event):
        """
        Обрабатывает события pygame, возникшие в ходе работы главного цикла окна.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.controls:
                if type(button) == view.Button:
                    button.call_action()

    def update(self):
        """
        Обновляет активное окно (элемент screen) в ходе главного цикла, не вызывая pygame.display.update().
        """
        for control in self.controls:
            control.focus(pygame.mouse.get_pos())
            control.show()

    def mainloop(self):
        """
        Главный цикл окна, 
        подготавливает и отправляет на обработку pygame события, вызывая метод self.handle(event), 
        обновляет окно, вызывая метод self.update() и обновляет дисплей.
        """
        finished = False
        while not finished:
            clock.tick(30)
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                self.handle(event)
            pygame.display.update()


class Game(Window):
    """
    Основное окно игры.
    """

    def __init__(self, screen, clock) -> None:
        super().__init__(screen, clock)
        self.world = data.deserialise()
        self.view = view.GameView(screen)

    def handle(self, event):
        super().handle(event)
        if event.type == pygame.QUIT:
            data.serialise(self.world)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass  # FIXME обработка выбора команд и передача команды в модель
        elif event.type == pygame.KEYDOWN:
            if event.key == '':  # text key
                pass  # FIXME обработка процесса ввода команды
            if event.key == '':  # enter key
                # FIXME обработка окончания ввода команды и передача команды в модель
                formated_command, responce = self.world.dispatch_command("") 
                self.view.add_command(formated_command)
                self.view.add_responce(responce)

    def update(self):
        super().update()
        self.world.update()
        self.view.update()


class StartMenu(Window):
    """
    Стартовое меню приложения, первым появляется на экране.
    """

    def start_game(self):
        game = Game(self.screen, self.clock)
        game.mainloop()

    def __init__(self, screen, clock) -> None:
        super().__init__(screen, clock)
        start_button = view.Button(
            screen, (10, 10, WIDTH-20, 60), self.start_game, "start game")
        self.controls.append(start_button)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
menu = StartMenu(screen, clock)
menu.mainloop()

pygame.quit()
