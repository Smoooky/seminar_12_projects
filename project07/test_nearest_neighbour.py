"""Тесты проекта 7 — «Ближайший сосед»."""

import numpy as np
import pytest
from nearest_neighbour import (
    accuracy,
    class_counts,
    make_blobs,
    pairwise_distances,
    predict,
    standardize,
    train_test_split,
)


def test_make_blobs_shapes() -> None:
    points, labels = make_blobs(seed=1, n=15)
    assert points.shape == (30, 2)
    assert labels.shape == (30,)
    assert class_counts(labels) == {0: 15, 1: 15}


def test_make_blobs_deterministic() -> None:
    first, _ = make_blobs(seed=7)
    second, _ = make_blobs(seed=7)
    assert np.array_equal(first, second)


def test_standardize_mean_and_std() -> None:
    points, _ = make_blobs(seed=3)
    scaled = standardize(points)
    assert np.allclose(scaled.mean(axis=0), 0.0, atol=1e-9)
    assert np.allclose(scaled.std(axis=0), 1.0, atol=1e-9)


def test_standardize_zero_variance() -> None:
    points = np.array([[1.0, 5.0], [1.0, 7.0], [1.0, 9.0]])
    scaled = standardize(points)
    assert np.array_equal(scaled[:, 0], [0.0, 0.0, 0.0])
    assert np.isfinite(scaled).all()


def test_pairwise_distances_values() -> None:
    a = np.array([[0.0, 0.0]])
    b = np.array([[3.0, 4.0], [0.0, 0.0]])
    result = pairwise_distances(a, b)
    assert result.shape == (1, 2)
    assert np.allclose(result, [[5.0, 0.0]])


def test_pairwise_distances_shape() -> None:
    result = pairwise_distances(np.zeros((3, 2)), np.ones((4, 2)))
    assert result.shape == (3, 4)


def test_pairwise_distances_diagonal_zero() -> None:
    points, _ = make_blobs(seed=2)
    distances = pairwise_distances(points, points)
    assert np.allclose(np.diag(distances), 0.0)
    assert np.allclose(distances, distances.T)


def test_train_test_split_sizes() -> None:
    points, labels = make_blobs(seed=0, n=20)
    train_x, test_x, train_y, test_y = train_test_split(points, labels)
    assert len(test_x) == 10            # 25% от 40
    assert len(train_x) == 30
    assert train_y.shape == (30,)
    assert test_y.shape == (10,)


def test_train_test_split_deterministic() -> None:
    points, labels = make_blobs(seed=0)
    a = train_test_split(points, labels, seed=5)
    b = train_test_split(points, labels, seed=5)
    assert np.array_equal(a[1], b[1])
    assert np.array_equal(a[3], b[3])


def test_predict_trivial() -> None:
    train_points = np.array([[0.0, 0.0], [10.0, 10.0]])
    train_labels = np.array([0, 1])
    test_points = np.array([[1.0, 1.0], [9.0, 9.0]])
    assert list(predict(train_points, train_labels, test_points)) == [0, 1]


def test_accuracy() -> None:
    result = accuracy(np.array([1, 0, 1]), np.array([1, 0, 0]))
    assert result == pytest.approx(2 / 3)
    assert type(result) is float


def test_pipeline_accuracy_on_blobs() -> None:
    points, labels = make_blobs(seed=0)
    train_x, test_x, train_y, test_y = train_test_split(points, labels, seed=0)
    predicted = predict(train_x, train_y, test_x)
    assert accuracy(test_y, predicted) > 0.9


def test_class_counts() -> None:
    assert class_counts(np.array([0, 0, 1, 2, 2, 2])) == {0: 2, 1: 1, 2: 3}
