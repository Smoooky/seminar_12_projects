"""Проект 4. «Таблица лиги» — турнирная таблица на Pandas.

Темы семинара 12: `pd.concat`, `rename`, `groupby(...).agg` с именованными
агрегатами, производные колонки через `np.where`, булевы фильтры,
`sort_values`.

На вход функциям приходит `DataFrame` с колонками
`home`, `away`, `home_goals`, `away_goals` — по строке на матч.
Пример собирает `sample_matches()`.

Правило то же: циклов по строкам нет, всё — операции над колонками и
группировки. Очки считаем футбольные: победа — 3, ничья — 1, поражение — 0.
"""

import numpy as np
import pandas as pd


def sample_matches() -> pd.DataFrame:
    """Маленький турнир из шести матчей. Дано — не трогайте."""
    return pd.DataFrame(
        {
            "home": ["Reds", "Reds", "Blues", "Blues", "Greens", "Greens"],
            "away": ["Blues", "Greens", "Reds", "Greens", "Reds", "Blues"],
            "home_goals": [3, 1, 1, 0, 2, 1],
            "away_goals": [0, 1, 2, 0, 0, 3],
        }
    )


def all_teams(matches: pd.DataFrame) -> list[str]:
    """Все названия команд, отсортированные по алфавиту."""
    raise NotImplementedError("Implement me")


def long_form(matches: pd.DataFrame) -> pd.DataFrame:
    """Развернуть матчи в таблицу «команда-матч».

    Одна строка на каждое участие команды в матче (то есть матчей в два раза
    больше строк). Колонки ровно такие: `team`, `opponent`, `goals`,
    `opponent_goals`. Порядок строк: сначала все хозяева по порядку матчей,
    затем все гости по порядку матчей. Индекс — обычный `0..n-1`.
    """
    raise NotImplementedError("Implement me")


def points_table(matches: pd.DataFrame) -> pd.Series:
    """Очки каждой команды, отсортированные по убыванию.

    Индекс — название команды, значения — сумма очков (победа 3, ничья 1).
    """
    raise NotImplementedError("Implement me")


def goals_by_team(matches: pd.DataFrame) -> pd.DataFrame:
    """Забитые/пропущенные мячи и разница на команду.

    Колонки: `scored`, `conceded`, `diff`; индекс — команда. Сортировка по
    `diff` по убыванию.
    """
    raise NotImplementedError("Implement me")


def head_to_head(matches: pd.DataFrame, team_a: str, team_b: str) -> pd.DataFrame:
    """Матчи только между `team_a` и `team_b` (в любом порядке), в том же виде.

    Порядок строк — как в исходной таблице.
    """
    raise NotImplementedError("Implement me")


def form(matches: pd.DataFrame, team: str) -> str:
    """Строка из `W`/`D`/`L` — результаты `team` по порядку матчей.

    Матчи, в которых команда не играла, пропускаются. Например, `"WDWL"`.
    """
    raise NotImplementedError("Implement me")


def winner(matches: pd.DataFrame) -> str:
    """Команда с наибольшим числом очков (при равенстве — первая в таблице)."""
    raise NotImplementedError("Implement me")
