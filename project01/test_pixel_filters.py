"""Тесты проекта 1 — «Фильтры»."""

import numpy as np
import pytest
from pixel_filters import (
    box_blur,
    brighten,
    check_image,
    count_dark,
    crop,
    edges,
    flip_left_right,
    flip_upside_down,
    invert,
    threshold,
    to_sepia,
)


def sample() -> np.ndarray:
    return np.array(
        [
            [0, 10, 20, 30],
            [40, 50, 60, 70],
            [80, 90, 100, 110],
        ],
        dtype=np.uint8,
    )


def test_check_image_ok() -> None:
    check_image(sample())


@pytest.mark.parametrize(
    "bad",
    [
        [[1, 2], [3, 4]],                     # список, не uint8
        np.arange(3, dtype=np.uint8),         # одномерный
        np.zeros((2, 2, 2), dtype=np.uint8),  # трёхмерный
        np.zeros((2, 2), dtype=np.int64),     # не тот тип
    ],
)
def test_check_image_rejects(bad) -> None:
    with pytest.raises(ValueError):
        check_image(bad)


def test_crop_values() -> None:
    piece = crop(sample(), 1, 1, 2, 2)
    assert np.array_equal(piece, [[50, 60], [90, 100]])


def test_crop_returns_view() -> None:
    image = sample()
    piece = crop(image, 0, 0, 2, 2)
    piece[0, 0] = 255
    assert image[0, 0] == 255


@pytest.mark.parametrize(
    "args",
    [(-1, 0, 2, 2), (0, -1, 2, 2), (0, 0, 0, 2), (0, 0, 2, 0), (2, 0, 2, 2), (0, 3, 2, 2)],
)
def test_crop_rejects(args) -> None:
    with pytest.raises(ValueError):
        crop(sample(), *args)


def test_flips() -> None:
    image = sample()
    assert np.array_equal(flip_left_right(image)[0], [30, 20, 10, 0])
    assert np.array_equal(flip_upside_down(image)[0], [80, 90, 100, 110])


def test_flip_is_view() -> None:
    image = sample()
    mirror = flip_left_right(image)
    mirror[0, 0] = 7
    assert image[0, -1] == 7


def test_invert() -> None:
    assert np.array_equal(invert(sample())[0], [255, 245, 235, 225])
    assert np.array_equal(invert(sample())[-1], [175, 165, 155, 145])


def test_brighten_clips_not_wraps() -> None:
    bright = np.array([[200, 250]], dtype=np.uint8)
    assert np.array_equal(brighten(bright, 100), [[255, 255]])
    assert np.array_equal(brighten(bright, -250), [[0, 0]])
    assert np.array_equal(brighten(bright, 100000), [[255, 255]])


def test_brighten_dtype() -> None:
    assert brighten(sample(), 5).dtype == np.uint8


def test_threshold_strict() -> None:
    assert np.array_equal(threshold(sample(), 50)[1], [0, 0, 255, 255])
    # ровно level не считается «ярче»
    assert np.array_equal(threshold(sample(), 10)[0], [0, 0, 255, 255])


def test_count_dark_is_int() -> None:
    result = count_dark(sample(), 50)
    assert result == 5
    assert type(result) is int


def test_box_blur_keeps_constant() -> None:
    flat = np.full((4, 4), 100, dtype=np.uint8)
    assert np.array_equal(box_blur(flat, 3), flat)
    assert box_blur(flat, 3).dtype == np.uint8


def test_box_blur_spreads_point() -> None:
    image = np.zeros((5, 5), dtype=np.uint8)
    image[2, 2] = 255
    blurred = box_blur(image, 3)
    assert blurred[2, 2] == 28          # 255 / 9, округлено
    assert blurred[0, 0] == 0           # угла пятно не достигает
    assert blurred.shape == image.shape


def test_box_blur_rejects_bad_size() -> None:
    with pytest.raises(ValueError):
        box_blur(sample(), 0)
    with pytest.raises(ValueError):
        box_blur(sample(), 2)


def test_edges() -> None:
    flat = np.full((4, 4), 7, dtype=np.uint8)
    assert np.array_equal(edges(flat), np.zeros((4, 4), dtype=np.uint8))

    step = np.zeros((4, 4), dtype=np.uint8)
    step[2:, 2:] = 255
    result = edges(step)
    assert result[2, 2] == 255          # 255 + 255, прижато к границе
    assert result.dtype == np.uint8


def test_to_sepia_shape_and_dtype() -> None:
    sepia = to_sepia(sample())
    assert sepia.shape == (3, 4, 3)
    assert sepia.dtype == np.uint8


def test_to_sepia_channels() -> None:
    sepia = to_sepia(sample())
    assert np.array_equal(sepia[0, 0], [0, 0, 0])
    assert np.array_equal(sepia[0, 1], [10, 8, 6])
    assert np.array_equal(sepia[-1, -1], [110, 88, 66])


def test_to_sepia_bright() -> None:
    white = np.full((1, 1), 255, dtype=np.uint8)
    assert np.array_equal(to_sepia(white)[0, 0], [255, 204, 153])
