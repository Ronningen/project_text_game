"""
Модуль для сериализации и десериализации игрового прогресса между входами и выходами из программы. 
"""
import model

PATH = ""  # FIXME


def deserialise() -> model.World:
    """Выгружает из системного файла состояние мира и инициализирует его.
    returns: world в состоянии на момент последнего выхода из игры."""
    # FIXME
    return model.World()


def serialise(world):
    """Сохраняет состояние мира в системный файл."""  # предпочтительно JSON
    # FIXME
    pass