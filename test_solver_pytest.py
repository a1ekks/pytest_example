from unittest import TestCase

import pytest

from solver import add, square_equation_solver, TYPE_ERROR_TEXT


@pytest.mark.parametrize('args, expected_result', [
    ((1, 2), 3),
    (('ttt', 'bbb'), 'tttbbb')
])
def test_ok(args, expected_result):
    res = add(*args)
    assert res == expected_result


class TestSquareEquationSolver:

    def test_raises_type_error(self):
        with pytest.raises(TypeError) as exc_info:
            square_equation_solver('', 1, 1.2)

        assert str(exc_info.value) == TYPE_ERROR_TEXT

    def test_result_is_tuple(self):
        res = square_equation_solver(0, 0, 0)
        assert isinstance(res, tuple)

    # @pytest.mark.parametrize("args, expected_result", [
    #     ((1, -3, -4), (4, -1)),
    #     ((0, 0, 1), (None, None))
    # ])
    @pytest.mark.parametrize("args, expected_result", [
        pytest.param((1, -3, -4), (4, -1), id="general"),
        pytest.param((0, 0, 1), (None, None), id="no results")
    ])
    def test_solves_ok(self, args, expected_result):
        res = square_equation_solver(*args)
        assert res == expected_result

