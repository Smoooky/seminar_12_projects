"""Тесты проекта 6 — «Судоку»."""

import numpy as np
import pytest
from sudoku import (
    blocks,
    conflicts,
    empty_count,
    is_valid,
    sample_board,
    sample_puzzle,
    solve,
)


def test_blocks_shape_and_first_box() -> None:
    boxed = blocks(sample_board())
    assert boxed.shape == (9, 9)
    assert np.array_equal(boxed[0], [5, 3, 4, 6, 7, 2, 1, 9, 8])


def test_blocks_last_box() -> None:
    boxed = blocks(sample_board())
    assert np.array_equal(boxed[8], [2, 8, 4, 6, 3, 5, 1, 7, 9])


def test_solved_board_is_valid() -> None:
    assert is_valid(sample_board())
    assert not conflicts(sample_board()).any()


def test_puzzle_is_valid() -> None:
    assert is_valid(sample_puzzle())


def test_conflicts_flags_duplicates_in_row() -> None:
    board = sample_board()
    board[0, 1] = 5                 # 5 стоит в строке дважды
    mask = conflicts(board)
    assert mask[0, 0]
    assert mask[0, 1]
    assert not is_valid(board)


def test_conflicts_flags_duplicate_in_column() -> None:
    board = sample_board()
    board[3, 0] = 5                 # 5 уже есть в колонке 0
    assert conflicts(board)[3, 0]
    assert not is_valid(board)


def test_conflicts_flags_duplicate_in_block() -> None:
    board = sample_board()
    board[2, 2] = 5                 # 5 уже есть в верхнем левом блоке
    assert conflicts(board)[2, 2]
    assert not is_valid(board)


def test_empty_count() -> None:
    assert empty_count(sample_board()) == 0
    assert empty_count(sample_puzzle()) == 5
    assert empty_count(np.zeros((9, 9), dtype=int)) == 81


def test_solve_solved_board_is_identity() -> None:
    assert np.array_equal(solve(sample_board()), sample_board())


def test_solve_puzzle_fills_and_agrees() -> None:
    puzzle = sample_puzzle()
    solved = solve(puzzle)
    assert empty_count(solved) == 0
    assert is_valid(solved)
    filled = puzzle != 0
    assert np.array_equal(solved[filled], puzzle[filled])


def test_solve_rejects_conflicting_board() -> None:
    board = np.zeros((9, 9), dtype=int)
    board[0, 0] = 5
    board[0, 1] = 5
    with pytest.raises(ValueError):
        solve(board)
