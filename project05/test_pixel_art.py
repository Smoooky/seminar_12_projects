"""Тесты проекта 5 — «Пиксель-арт»."""

import numpy as np
import pytest
from pixel_art import (
    colours_used,
    downsample,
    nearest_palette_index,
    palette,
    quantize,
    sample_gray,
    sample_rgb,
    to_ascii,
)


def test_sample_gray() -> None:
    image = sample_gray()
    assert image.shape == (8, 8)
    assert image.dtype == np.uint8
    assert image[0, 0] == 0
    assert image[0, -1] == 224


def test_downsample_shape_and_dtype() -> None:
    small = downsample(sample_gray(), 2)
    assert small.shape == (4, 4)
    assert small.dtype == np.uint8


def test_downsample_values() -> None:
    small = downsample(sample_gray(), 2)
    assert np.array_equal(small[0], [16, 80, 144, 208])
    assert np.array_equal(small[3], [16, 80, 144, 208])


def test_downsample_factor_one_is_identity() -> None:
    image = sample_gray()
    assert np.array_equal(downsample(image, 1), image)


def test_downsample_rejects_bad_factor() -> None:
    with pytest.raises(ValueError):
        downsample(sample_gray(), 0)
    with pytest.raises(ValueError):
        downsample(sample_gray(), 3)


def test_to_ascii_first_line() -> None:
    art = to_ascii(sample_gray())
    lines = art.splitlines()
    assert len(lines) == 8
    assert lines[0] == " .:-+*#%"
    assert all(line == lines[0] for line in lines)


def test_to_ascii_custom_ramp() -> None:
    white = np.full((1, 1), 255, dtype=np.uint8)
    black = np.full((1, 1), 0, dtype=np.uint8)
    assert to_ascii(white, "01") == "1"
    assert to_ascii(black, "01") == "0"


def test_nearest_palette_index() -> None:
    colours = np.array(
        [[10, 10, 10], [250, 10, 10], [0, 240, 0], [5, 5, 240], [240, 240, 240]]
    )
    result = nearest_palette_index(colours, palette())
    assert list(result) == [0, 1, 2, 3, 4]


def test_quantize_shape_dtype() -> None:
    result = quantize(sample_rgb(), palette())
    assert result.shape == (2, 2, 3)
    assert result.dtype == np.uint8


def test_quantize_values() -> None:
    result = quantize(sample_rgb(), palette())
    assert np.array_equal(result[0, 0], [0, 0, 0])
    assert np.array_equal(result[0, 1], [255, 255, 255])
    assert np.array_equal(result[1, 0], [0, 0, 0])
    assert np.array_equal(result[1, 1], [255, 0, 0])


def test_colours_used() -> None:
    assert colours_used(sample_rgb()) == [
        (0, 0, 0),
        (10, 10, 10),
        (250, 0, 0),
        (255, 255, 255),
    ]


def test_colours_used_after_quantize() -> None:
    assert colours_used(quantize(sample_rgb(), palette())) == [
        (0, 0, 0),
        (255, 0, 0),
        (255, 255, 255),
    ]
