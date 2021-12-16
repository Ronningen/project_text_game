"""
Главный модуль, содержит и управляет окнами приложения.
Среди окон есть меню и главное окно игры, связывающее игровую модель с интерфейсом.
"""
import pygame
pygame.init()

import view
import model
import data



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
        self.input_text = ''

    def handle(self, event):
        super().handle(event)
        if event.type == pygame.QUIT:
            data.serialise(self.world)
        elif not self.temp_buttons_active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                command_list = self.world.dispatch_command(self.input_text)
                if len(command_list) > 0:
                    self.temp_buttons_active = True
                    self.add_temp_buttons(command_list)
                self.input_text = ''
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            else:
                self.input_text += event.unicode

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
        self.view.blit_input_text(self.input_text)
        if self.temp_buttons_chosen:
            self.remove_temp_buttons()
        command = self.world.get_command()
        if command and command != 'None':
            self.view.add_command(command)
        response = self.world.get_response()
        if response and response != 'None':
            self.view.add_response(response)
           
    def add_temp_buttons(self, command_list):
        top = view.buttonrow_top
        width = view.textlines_width/len(command_list)
        height = view.textlines_height
        for cmd in command_list:
            i = command_list.index(cmd)
            left = width*i
            button = view.Button(self.screen, (left,top,width,height), self.temp_button_func(cmd.get_func()), cmd.get_name())
            self.controls.append(button)
            self.temp_controls.append(button)

    def remove_temp_buttons(self):
        self.temp_buttons_active = False
        self.temp_buttons_chosen = False
        for control in self.temp_controls:
            self.controls.remove(control)
        self.temp_controls.clear() 
        

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


screen = pygame.display.set_mode((view.WIDTH, view.HEIGHT))
clock = pygame.time.Clock()
menu = StartMenu(screen, clock)
menu.mainloop()

pygame.quit()