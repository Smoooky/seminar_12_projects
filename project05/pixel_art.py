"""Проект 5. «Пиксель-арт» — картинки из массивов.

Темы семинара 12: `reshape` и оси, `.mean(axis=...)`, `astype`, broadcasting
через `[:, None, :]`, `argmin`, `np.unique(axis=0)`, сборка строк.

Изображение — массив `uint8`: серое `(h, w)` или цветное `(h, w, 3)`.
Два готовых примера дают `sample_gray()` и `sample_rgb()`, палитру — `palette()`.
"""

import numpy as np


def sample_gray() -> np.ndarray:
    """Серый оттенок-градиент 8x8 (слева темно, справа светло). Дано."""
    columns = np.arange(8, dtype=np.uint8) * 32
    return np.tile(columns, (8, 1))


def sample_rgb() -> np.ndarray:
    """Крошечное RGB-изображение 2x2. Дано."""
    return np.array(
        [
            [[0, 0, 0], [255, 255, 255]],
            [[10, 10, 10], [250, 0, 0]],
        ],
        dtype=np.uint8,
    )


def palette() -> np.ndarray:
    """Палитра из пяти цветов, форма `(5, 3)`. Дано."""
    return np.array(
        [
            [0, 0, 0],
            [255, 0, 0],
            [0, 255, 0],
            [0, 0, 255],
            [255, 255, 255],
        ],
        dtype=np.uint8,
    )


def downsample(image: np.ndarray, factor: int) -> np.ndarray:
    """Уменьшить изображение в `factor` раз по каждой стороне.

    Каждый блок `factor`x`factor` превращается в один пиксель — его среднее,
    округлённое до `uint8`. Стороны должны делиться на `factor`, иначе
    `ValueError`. Циклов по пикселям нет — только `reshape` и редукции.
    """
    raise NotImplementedError("Implement me")


def to_ascii(image: np.ndarray, ramp: str = " .:-=+*#%@") -> str:
    """Превратить серое изображение в ASCII-картинку.

    Значение `value` (0..255) отображается на символ с индексом
    `value * len(ramp) // 256`. Строки соединяются через `"\\n"`.
    """
    raise NotImplementedError("Implement me")


def nearest_palette_index(colours: np.ndarray, pal: np.ndarray) -> np.ndarray:
    """Для каждого цвета (`n`, 3) — индекс ближайшего цвета палитры (`m`, 3).

    Близость — евклидово расстояние по RGB. Ответ — целый массив длины `n`.
    """
    raise NotImplementedError("Implement me")


def quantize(image: np.ndarray, pal: np.ndarray) -> np.ndarray:
    """Заменить каждый пиксель (`h`, `w`, 3) ближайшим цветом палитры.

    Форма сохраняется, тип — `uint8`.
    """
    raise NotImplementedError("Implement me")


def colours_used(image: np.ndarray) -> list[tuple[int, int, int]]:
    """Уникальные цвета картинки (`h`, `w`, 3) как отсортированный список кортежей."""
    raise NotImplementedError("Implement me")
