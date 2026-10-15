"""Тесты проекта 3 — «Wrapped»."""

import numpy as np
import pandas as pd
from wrapped_stats import (
    favourite_weekday,
    minutes_by_artist,
    minutes_by_genre,
    minutes_matrix,
    new_artists,
    sample_plays,
    top_artists,
    total_minutes,
)


def test_total_minutes() -> None:
    total = total_minutes(sample_plays())
    assert total == 30.0
    assert type(total) is float


def test_minutes_by_artist_values() -> None:
    by_artist = minutes_by_artist(sample_plays())
    assert by_artist.loc["Kino"] == 11.0
    assert by_artist.loc["Mira"] == 7.0
    assert by_artist.loc["Neon"] == 6.0
    assert by_artist.loc["Zen"] == 6.0


def test_minutes_by_artist_sorted() -> None:
    values = list(minutes_by_artist(sample_plays()).to_numpy())
    assert values == sorted(values, reverse=True)
    assert minutes_by_artist(sample_plays()).index[0] == "Kino"


def test_top_artists() -> None:
    assert top_artists(sample_plays(), 2) == ["Kino", "Mira"]


def test_top_artists_default_three() -> None:
    assert len(top_artists(sample_plays())) == 3


def test_minutes_by_genre() -> None:
    by_genre = minutes_by_genre(sample_plays())
    assert by_genre.loc["pop"] == 13.0
    assert by_genre.loc["rock"] == 11.0
    assert by_genre.loc["jazz"] == 6.0
    assert by_genre.index[0] == "pop"


def test_favourite_weekday() -> None:
    assert favourite_weekday(sample_plays()) == "Friday"


def test_new_artists() -> None:
    assert new_artists(sample_plays()) == ["Mira", "Zen"]
    assert new_artists(sample_plays(), "2024-01-01") == ["Kino", "Mira", "Neon", "Zen"]


def test_minutes_matrix_shape() -> None:
    matrix = minutes_matrix(sample_plays())
    assert isinstance(matrix, np.ndarray)
    assert matrix.shape == (8, 1)
    assert matrix.sum() == 30.0
