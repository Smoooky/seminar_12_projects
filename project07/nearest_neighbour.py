"""Проект 7. «Ближайший сосед» — простейший классификатор на NumPy.

Темы семинара 12: broadcasting через `[:, None, :]`, попарные расстояния,
`argmin(axis=1)`, редукции, `np.random.default_rng`, сравнение массивов.

Данные — точки `(n, 2)` (координаты) и метки `(n,)` (классы). Два готовых
кластера возвращает `make_blobs()`. Алгоритм: тестовая точка получает метку
ближайшей обучающей точки.
"""

import numpy as np


def make_blobs(seed: int = 0, n: int = 20) -> tuple[np.ndarray, np.ndarray]:
    """Два кластера по `n` точек: вокруг (0,0) и (5,5). Дано — не трогайте."""
    rng = np.random.default_rng(seed)
    first = rng.normal(loc=[0.0, 0.0], scale=0.6, size=(n, 2))
    second = rng.normal(loc=[5.0, 5.0], scale=0.6, size=(n, 2))
    points = np.vstack([first, second])
    labels = np.array([0] * n + [1] * n)
    return points, labels


def standardize(points: np.ndarray) -> np.ndarray:
    """Вычесть среднее и поделить на стандартное отклонение (по столбцам).

    Если у какого-то столбца разброс нулевой, делить на ноль нельзя — там
    оставляем значения как есть (делим на 1).
    """
    raise NotImplementedError("Implement me")


def pairwise_distances(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Матрица `(len(a), len(b))` евклидовых расстояний между точками.

    Циклов нет — вся разность через broadcasting `a[:, None, :] - b[None, :, :]`.
    """
    raise NotImplementedError("Implement me")


def train_test_split(
    points: np.ndarray,
    labels: np.ndarray,
    test_fraction: float = 0.25,
    seed: int = 0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Разбить данные на обучение и тест.

    Возврат: `(train_points, test_points, train_labels, test_labels)`.
    Число тестовых точек — `int(len(points) * test_fraction)`. Перемешивание
    детерминировано по `seed` (`rng.permutation`).
    """
    raise NotImplementedError("Implement me")


def predict(
    train_points: np.ndarray,
    train_labels: np.ndarray,
    test_points: np.ndarray,
) -> np.ndarray:
    """Метка для каждой тестовой точки — метка ближайшей обучающей."""
    raise NotImplementedError("Implement me")


def accuracy(true_labels: np.ndarray, predicted: np.ndarray) -> float:
    """Доля совпадений, обычный `float`."""
    raise NotImplementedError("Implement me")


def class_counts(labels: np.ndarray) -> dict[int, int]:
    """Сколько точек каждого класса: `{метка: количество}`."""
    raise NotImplementedError("Implement me")
