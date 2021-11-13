"""
Интерфейс с пользователем, выводящий данные, полученные от ядра, и передает ему команды пользователя.
"""
import pygame


class viewmanager:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

    def update(self, data):
        """
        Выводит информацию снизу вверх:
            Сначала выводит поле интеракции с игроком (поле ввода текста или список действий для выбора),
            Отчеркивание,
            История вводимых команд и ответов игры.

        Здесь же реализуются прочие визуальные и звуковые эффекты.

        data: новые данные и инструкции для отображения
        """ #тут же, если будет нужен, вывод состояния героя и или инвенторя

        # FIXME
        pass