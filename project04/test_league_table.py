"""Тесты проекта 4 — «Таблица лиги»."""

from league_table import (
    all_teams,
    form,
    goals_by_team,
    head_to_head,
    long_form,
    points_table,
    sample_matches,
    winner,
)


def test_all_teams() -> None:
    assert all_teams(sample_matches()) == ["Blues", "Greens", "Reds"]


def test_long_form_shape_and_columns() -> None:
    long = long_form(sample_matches())
    assert list(long.columns) == ["team", "opponent", "goals", "opponent_goals"]
    assert len(long) == 12                 # 6 матчей × 2 участия
    assert list(long.index) == list(range(12))


def test_long_form_first_home_row() -> None:
    first = long_form(sample_matches()).iloc[0]
    assert (first["team"], first["opponent"]) == ("Reds", "Blues")
    assert (first["goals"], first["opponent_goals"]) == (3, 0)


def test_long_form_first_away_row() -> None:
    first_away = long_form(sample_matches()).iloc[6]
    assert (first_away["team"], first_away["opponent"]) == ("Blues", "Reds")
    assert (first_away["goals"], first_away["opponent_goals"]) == (0, 3)


def test_points_table_values() -> None:
    table = points_table(sample_matches())
    assert table.loc["Reds"] == 7
    assert table.loc["Greens"] == 5
    assert table.loc["Blues"] == 4


def test_points_table_sorted() -> None:
    table = points_table(sample_matches())
    assert list(table.index) == ["Reds", "Greens", "Blues"]
    assert list(table.to_numpy()) == [7, 5, 4]


def test_goals_by_team() -> None:
    table = goals_by_team(sample_matches())
    assert list(table.columns) == ["scored", "conceded", "diff"]
    assert table.loc["Reds", "scored"] == 6
    assert table.loc["Reds", "conceded"] == 4
    assert table.loc["Reds", "diff"] == 2
    assert table.loc["Blues", "diff"] == -2
    assert list(table.index) == ["Reds", "Greens", "Blues"]


def test_head_to_head_both_orders() -> None:
    pairs = head_to_head(sample_matches(), "Reds", "Blues")
    assert len(pairs) == 2
    assert set(pairs["home"]) | set(pairs["away"]) >= {"Reds", "Blues"}
    assert set(pairs["home"]) | set(pairs["away"]) == {"Reds", "Blues"}


def test_head_to_head_is_symmetric() -> None:
    a = head_to_head(sample_matches(), "Reds", "Blues")
    b = head_to_head(sample_matches(), "Blues", "Reds")
    assert len(a) == len(b)


def test_form() -> None:
    matches = sample_matches()
    assert form(matches, "Reds") == "WDWL"
    assert form(matches, "Blues") == "LLDW"
    assert form(matches, "Greens") == "DDWL"


def test_winner() -> None:
    assert winner(sample_matches()) == "Reds"
