"""Проект 6. «Судоку» — проверка и решение на NumPy.

Темы семинара 12: `reshape(3,3,3,3).swapaxes(1,2)` для сборки блоков,
broadcasting-сравнения `grid[:, :, None] == grid[:, None, :]`,
`np.count_nonzero`, `np.argwhere`, рекурсия.

Поле — целочисленный массив `(9, 9)`, где `0` — пустая клетка. Готовое
корректное поле даёт `sample_board()`, поле с пропусками — `sample_puzzle()`.
"""

import numpy as np


def sample_board() -> np.ndarray:
    """Корректно решённое судоку 9x9. Дано — не трогайте."""
    return np.array(
        [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ],
        dtype=int,
    )


def sample_puzzle() -> np.ndarray:
    """То же поле с пятью пустыми клетками. Дано."""
    board = sample_board()
    for row, col in [(0, 0), (0, 1), (1, 4), (4, 4), (8, 8)]:
        board[row, col] = 0
    return board


def blocks(board: np.ndarray) -> np.ndarray:
    """Собрать 3x3-блоки в строки: результат `(9, 9)`.

    Строка `k` результата — это клетки `k`-го блока, прочитанные слева
    направо и сверху вниз. Блоки нумеруются слева направо, сверху вниз.
    """
    raise NotImplementedError("Implement me")


def conflicts(board: np.ndarray) -> np.ndarray:
    """Булева маска `(9, 9)`: клетки, дублирующие своё число в строке/столбце/блоке.

    Нули игнорируются. Клетка помечена `True`, если её значение совпадает с
    ещё одной клеткой в той же строке, столбце или блоке.
    """
    raise NotImplementedError("Implement me")


def is_valid(board: np.ndarray) -> bool:
    """Нет ли ни одного конфликта (пустые клетки не мешают)."""
    raise NotImplementedError("Implement me")


def empty_count(board: np.ndarray) -> int:
    """Сколько пустых клеток. Ответ — обычный `int`."""
    raise NotImplementedError("Implement me")


def solve(board: np.ndarray) -> np.ndarray:
    """Решить судоку и вернуть заполненное поле `(9, 9)`.

    Если решения нет или поле уже противоречиво — `ValueError`. Здесь
    рекурсивный перебор уместен: это не поэлементная векторная операция.
    """
    raise NotImplementedError("Implement me")
