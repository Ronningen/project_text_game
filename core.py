"""
Главный модуль, содержит и управляет окнами приложения.
Среди окон есть меню и главное окно игры, связывающее игровую модель с интерфейсом.
"""
import pygame
pygame.init()

import view
import model
import data


WIDTH, HEIGHT = 800, 600


class Window:
    """
    Базовый класс, управляющий активным окном pygame.
    Содержит и отображает экземпляры view.WindowElement - список controls.
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
        screen.fill((0,0,0))
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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                self.handle(event)
            self.update()
            pygame.display.update()


class Game(Window):
    """
    Основное окно игры.
    """

    def __init__(self, screen, clock) -> None:
        super().__init__(screen, clock)
        self.world = data.deserialise()
        self.view = view.GameView(screen)
        self.temp_buttons_active = False #флаг активности выбора команды - ручной ввод запрещен если True
        self.temp_buttons_chosen = False #флаг события нажатия кнопки - True если кнопка была нажата - кнопки должны быть стеры если True
        self.temp_controls = []
        self.command_text = ''

    def handle(self, event):
        super().handle(event)
        if event.type == pygame.QUIT:
            data.serialise(self.world)
        elif not self.temp_buttons_active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # FIXME - не нужно что-то делать, если команда - пустая строка
                command_list = self.world.dispatch_command(self.command_text)
                i = 2
                if len(command_list) > 0:
                    self.temp_buttons_active = True
                    for cmd in command_list:
                        i -= 1
                        button = view.Button(screen, (100*i,100*i,100,100), self.temp_button_func(cmd.get_func()), cmd.get_name())
                        # FIXME - вывод кнопок должен не мешать текту
                        self.controls.append(button)
                        self.temp_controls.append(button)
                        print(len(self.controls))
                self.command_text = ''
            elif event.key == pygame.K_BACKSPACE:
                self.command_text = self.command_text[:-1]
            else:
                self.command_text += event.unicode

    def temp_button_func(self, func):
        """
        Добавляет в функцию изменение флага, за которым должны стираться все временные кнопки
        """
        def func_with_changing_flag():
            func()
            self.temp_buttons_chosen = True
        return func_with_changing_flag

    def update(self):
        super().update()
        self.view.update()
        if self.temp_buttons_chosen:
            self.temp_buttons_active = False
            self.temp_buttons_chosen = False
            for control in self.temp_controls:
                self.controls.remove(control)
            self.temp_controls.clear()
        command = self.world.get_command()
        if command and command != 'None':
            self.view.add_command(command)
        response = self.world.get_response()
        if response and response != 'None':
            self.view.add_response(response)


class StartMenu(Window):
    """
    Стартовое меню приложения, первым появляется на экране.
    """

    def start_game(self):
        """
        Открывает окно игры, скрывая меню соответсвенно. По закрытию окна игры снова появляется меню.
        """
        game = Game(self.screen, self.clock)
        game.mainloop()

    def __init__(self, screen, clock) -> None:
        super().__init__(screen, clock)
        start_button = view.Button(
            screen, (10, 10, screen.get_width() - 20, 60), self.start_game, "start game")
        self.controls.append(start_button)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
menu = StartMenu(screen, clock)
menu.mainloop()

pygame.quit()