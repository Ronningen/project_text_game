"""
Главный модуль, контрорлирует и связывает модель и модуль отображения.
Здесь запускается главный процесс.
"""
import datamanager
import model
import view
import pygame

WIDTH, HEIGHT = 400, 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
finished = False

world = datamanager.deserialise()
viewmanager = view.viewmanager(screen)

while not finished:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            datamanager.serialise(world)
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass  # FIXME обработка выбора команд и передача команды в модель
        elif event.type == pygame.KEYDOWN:
            if event.key == '':  # text key
                pass  # FIXME обработка процесса ввода команды
            if event.key == '':  # enter key
                pass  # FIXME обработка окончания ввода команды и передача команды в модель

    world.update()

    screen.fill((0, 0, 0))
    viewmanager.update('')  # FIXME надо передавать данные на вывод
    pygame.display.update()

pygame.quit()
