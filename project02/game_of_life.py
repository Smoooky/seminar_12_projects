"""Проект 2. «Жизнь» — клеточный автомат Конвея.

Темы семинара 12: `np.pad` и скользящие окна, ловушка «булевы массивы не
складываются», `np.where`, редукции, `np.array_equal`.

Поле — булев массив: `True` — живая клетка. За границей поля всегда «мёртво»
(её добавляет `np.pad`). Правила перехода в следующее поколение:

* живая клетка выживает, если у неё 2 или 3 живых соседа;
* мёртвая оживает, если у неё ровно 3 живых соседа;
* в остальных случаях клетка мертва.

Циклов по клеткам быть не должно: число живых соседей считается восемью
сдвинутыми копиями поля из `np.pad`, сложенными вместе.
"""

import numpy as np


def empty_board(size: int) -> np.ndarray:
    """Пустое поле `size`x`size` из `False`. Дано — не трогайте."""
    return np.zeros((size, size), dtype=bool)


def glider() -> np.ndarray:
    """Глайдер — фигура, которая за 4 поколения сдвигается на (1, 1). Дано."""
    board = empty_board(6)
    for row, col in [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]:
        board[row, col] = True
    return board


def blinker() -> np.ndarray:
    """Мигалка — три клетки в ряд. Дано."""
    board = empty_board(5)
    board[2, 1:4] = True
    return board


def block() -> np.ndarray:
    """Блок 2x2 — неподвижная фигура. Дано."""
    board = empty_board(4)
    board[1:3, 1:3] = True
    return board


def neighbours(board: np.ndarray) -> np.ndarray:
    """Сколько живых соседей у каждой клетки (без самой клетки).

    Тип результата — целый, форма та же, что у поля. За границей поля соседей
    нет, поэтому рамка из нулей.
    """
    raise NotImplementedError("Implement me")


def step(board: np.ndarray) -> np.ndarray:
    """Одно поколение вперёд. На входе и выходе — булево поле."""
    raise NotImplementedError("Implement me")


def run(board: np.ndarray, steps: int) -> np.ndarray:
    """Прокрутить `steps` поколений и вернуть итоговое поле."""
    raise NotImplementedError("Implement me")


def history(board: np.ndarray, steps: int) -> list[np.ndarray]:
    """Список полей: исходное, затем после каждого шага. Длина `steps + 1`.

    Исходное поле кладётся **копией**, чтобы дальше его нельзя было задеть.
    """
    raise NotImplementedError("Implement me")


def population(board: np.ndarray) -> int:
    """Сколько живых клеток. Ответ — обычный `int`."""
    raise NotImplementedError("Implement me")


def is_stable(board: np.ndarray) -> bool:
    """Не меняется ли поле за один шаг."""
    raise NotImplementedError("Implement me")
