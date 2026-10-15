"""Проект 1. «Фильтры» — картинка как массив `uint8`.

Темы семинара 12: `view` против копии, переполнение `uint8`, булевы маски,
`np.where`/`np.count_nonzero`, броадкаст, `np.pad` и скользящие окна, сборка
цвета через `np.dstack`.

Картинка — двумерный массив `uint8` формы `(высота, ширина)`: строка на ряд
пикселей, число — яркость от 0 (чёрный) до 255 (белый). Циклов по пикселям нет
нигде: только срезы, арифметика над массивом целиком и булевы маски.
"""

import numpy as np
import numpy.typing as npt

# Тип «картинка»: двумерный массив байтов. Просто псевдоним, не класс.
Image = npt.NDArray[np.uint8]


def check_image(image: npt.ArrayLike) -> None:
    """Проверить, что это двумерный массив `uint8`. Иначе — `ValueError`.

    Эту проверку зовут все остальные функции в самом начале.
    """
    raise NotImplementedError("Implement me")


def crop(image: Image, top: int, left: int, height: int, width: int) -> Image:
    """Прямоугольный кусок картинки — **`view`**, а не копия.

    Правка куска должна быть видна в исходной картинке. Неположительные
    `height`/`width`, отрицательные `top`/`left` и выход за края — `ValueError`.
    """
    raise NotImplementedError("Implement me")


def flip_left_right(image: Image) -> Image:
    """Зеркало по горизонтали. Тоже `view` (срез с шагом `-1`)."""
    raise NotImplementedError("Implement me")


def flip_upside_down(image: Image) -> Image:
    """Зеркало по вертикали. Тоже `view`."""
    raise NotImplementedError("Implement me")


def invert(image: Image) -> Image:
    """Негатив: 0 становится 255, 255 — нулём."""
    raise NotImplementedError("Implement me")


def brighten(image: Image, amount: int) -> Image:
    """Прибавить `amount` к каждому пикселю с прижатием к 0..255.

    `amount` бывает и отрицательным, и очень большим по модулю: `+100000`
    обязан дать белую картинку, а не упасть. Прибавление в `uint8` завернётся
    по кругу — считайте в типе пошире и прижимайте результат.
    """
    raise NotImplementedError("Implement me")


def threshold(image: Image, level: int) -> Image:
    """Чёрно-белое без полутонов: **строго ярче** `level` → 255, иначе 0."""
    raise NotImplementedError("Implement me")


def count_dark(image: Image, level: int) -> int:
    """Сколько пикселей **строго темнее** `level`. Ответ — обычный `int`."""
    raise NotImplementedError("Implement me")


def box_blur(image: Image, size: int) -> Image:
    """Размытие усреднением окна `size`x`size` вокруг каждого пикселя.

    Края продлеваются (`np.pad(..., mode="edge")`), чтобы размер не менялся.
    `size` — нечётное положительное, иначе `ValueError`. Сумма по окну
    считается в широком типе, результат округляется и возвращается в `uint8`.
    """
    raise NotImplementedError("Implement me")


def edges(image: Image) -> Image:
    """Обводка контуров: модуль разности с соседом слева плюс сверху.

    `gx = image - np.roll(image, 1, axis=1)`, `gy` — то же по оси 0. Значения
    берутся по модулю, складываются и прижимаются к 255. Считайте в знаковом
    типе: в `uint8` разность завернётся.
    """
    raise NotImplementedError("Implement me")


def to_sepia(image: Image) -> Image:
    """Из чёрно-белой — тёплая цветная: каналы `[v, 0.8*v, 0.6*v]`.

    Возвращает массив формы `(высота, ширина, 3)` типа `uint8`. Каналы удобно
    собрать через `np.dstack`.
    """
    raise NotImplementedError("Implement me")
