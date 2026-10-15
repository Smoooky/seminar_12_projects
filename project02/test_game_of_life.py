"""Тесты проекта 2 — «Жизнь»."""

import numpy as np
from game_of_life import (
    blinker,
    block,
    empty_board,
    glider,
    history,
    is_stable,
    neighbours,
    population,
    run,
    step,
)


def test_empty_board() -> None:
    board = empty_board(4)
    assert board.shape == (4, 4)
    assert board.dtype == bool
    assert not board.any()


def test_neighbours_full_block() -> None:
    board = np.ones((3, 3), dtype=bool)
    count = neighbours(board)
    assert count.dtype.kind in "iu"       # целый тип, не bool
    assert count[1, 1] == 8               # центр
    assert count[0, 0] == 3               # угол — соседей вне поля нет
    assert count[0, 1] == 5               # край


def test_neighbours_ignores_self() -> None:
    board = np.zeros((3, 3), dtype=bool)
    board[1, 1] = True
    count = neighbours(board)
    assert count[1, 1] == 0               # клетка сама себя не считает
    assert count.sum() == 8               # зато её «видят» все восемь соседей


def test_step_blinker_becomes_vertical() -> None:
    vertical = step(blinker())
    assert np.array_equal(vertical[1:4, 2], [True, True, True])
    assert population(vertical) == 3


def test_blinker_period_two() -> None:
    assert np.array_equal(run(blinker(), 2), blinker())
    assert not np.array_equal(run(blinker(), 1), blinker())


def test_block_is_stable() -> None:
    assert is_stable(block())
    assert np.array_equal(run(block(), 10), block())


def test_blinker_is_not_stable() -> None:
    assert not is_stable(blinker())


def test_glider_translates_diagonally() -> None:
    moved = run(glider(), 4)
    expected = empty_board(6)
    for row, col in [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]:
        expected[row, col] = True
    assert np.array_equal(moved, expected)


def test_glider_keeps_population() -> None:
    assert population(glider()) == 5
    assert population(run(glider(), 4)) == 5


def test_population_is_int() -> None:
    result = population(glider())
    assert result == 5
    assert type(result) is int


def test_history_frames() -> None:
    frames = history(blinker(), 2)
    assert len(frames) == 3                # исходное + 2 шага
    assert np.array_equal(frames[0], blinker())
    assert np.array_equal(frames[2], blinker())
    assert not np.array_equal(frames[1], blinker())


def test_history_first_frame_is_copy() -> None:
    source = blinker()
    frames = history(source, 1)
    frames[0][0, 0] = True                 # портим «исходное» в списке
    assert source[0, 0] == False           # сам вход не пострадал


def test_throwing_off_alive_cell_thins_population() -> None:
    board = empty_board(3)
    board[1, 1] = True                     # одинокая клетка гибнет
    assert population(step(board)) == 0
