"""Проект 3. «Wrapped» — личная статистика прослушиваний на Pandas.

Темы семинара 12 (Pandas): `read_csv`-подобная работа с таблицей, новая
колонка из существующих, фильтры, `isin`, `nlargest`, `set_index`/`loc`,
`groupby(...).agg`, `value_counts`, `dt`-аксессор и `to_numpy`.

На вход функциям приходит `DataFrame` с колонками
`track`, `artist`, `genre`, `minutes`, `date`. Готовый маленький пример
собирает `sample_plays()` — им можно пользоваться и в своих опытах.

Правило то же, что и в задачах: циклов по строкам нет, всё — операции над
колонками и группировки.
"""

import numpy as np
import pandas as pd


def sample_plays() -> pd.DataFrame:
    """Маленький журнал прослушиваний для опытов. Дано — не трогайте."""
    return pd.DataFrame(
        {
            "track": ["A", "B", "C", "D", "E", "F", "G", "H"],
            "artist": ["Neon", "Neon", "Kino", "Kino", "Kino", "Mira", "Mira", "Zen"],
            "genre": ["pop", "pop", "rock", "rock", "rock", "pop", "pop", "jazz"],
            "minutes": [3.5, 2.5, 4.0, 4.0, 3.0, 5.0, 2.0, 6.0],
            "date": [
                "2024-01-05",
                "2024-01-12",
                "2024-02-10",
                "2024-03-01",
                "2024-08-01",
                "2024-08-15",
                "2024-09-01",
                "2024-11-20",
            ],
        }
    )


def total_minutes(plays: pd.DataFrame) -> float:
    """Суммарное время прослушивания в минутах, обычный `float`."""
    raise NotImplementedError("Implement me")


def minutes_by_artist(plays: pd.DataFrame) -> pd.Series:
    """Минуты по каждому артисту, отсортированные по убыванию.

    Индекс — имя артиста, значения — сумма минут.
    """
    raise NotImplementedError("Implement me")


def top_artists(plays: pd.DataFrame, n: int = 3) -> list[str]:
    """Имена `n` самых прослушиваемых артистов, по убыванию минут."""
    raise NotImplementedError("Implement me")


def minutes_by_genre(plays: pd.DataFrame) -> pd.Series:
    """Минуты по жанрам, по убыванию."""
    raise NotImplementedError("Implement me")


def favourite_weekday(plays: pd.DataFrame) -> str:
    """Название дня недели, в который набежало больше всего минут.

    Дату получите через `pd.to_datetime`, день недели — через аксессор `.dt`.
    """
    raise NotImplementedError("Implement me")


def new_artists(plays: pd.DataFrame, split: str = "2024-07-01") -> list[str]:
    """Артисты, впервые услышанные не раньше `split` (первое прослушивание).

    Возвращается отсортированный по алфавиту список имён.
    """
    raise NotImplementedError("Implement me")


def minutes_matrix(plays: pd.DataFrame) -> "np.ndarray":
    """Колонка минут как обычный `ndarray` формы `(n, 1)` (`to_numpy`).

    Дальше с этим массивом работает вся NumPy-половина лекции.
    """
    raise NotImplementedError("Implement me")
