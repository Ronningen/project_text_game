"""
Модуль для сериализации и десериализации игрового прогресса между входами и выходами из программы. 
"""

import pickle
import model
def deserialise() -> model.World:
    """Выгружает из системного файла world.saviour состояние мира и инициализирует его.
    returns: world в состоянии на момент последнего выхода из игры."""
    return None
    with open('world.saviour', 'rb') as f:
        world = pickle.load(f)
        return world


def serialise(world):
    """Сохраняет состояние мира в системный файл."""

    with open('world.saviour', 'wb') as f:
        pickle.dump(world, f)