"""
Модуль для сериализации и десериализации игрового прогресса между входами и выходами из программы. 
"""

import pickle
import model
import json

def deserialise() -> model.World:
    """Выгружает из системного файла world.saviour состояние мира и инициализирует его.
    returns: world в состоянии на момент последнего выхода из игры."""
    with open('world.saviour', 'r') as f:
        world = json.load(f)
        return world


def serialise(world):
    """Сохраняет состояние мира в системный файл."""

    with open('world.saviour', 'w') as f:
        json.dump(world, f)

