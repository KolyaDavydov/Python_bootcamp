"""для запуска теста требуется установленный pytest
из папки src выполнить: 'pytest-3 tests.py'
"""

import ex00
from ex01 import split_booty


def test_ex00():
    purse = {}
    purse = ex00.add_ingot({'gold_ingots': 10})
    assert {'gold_ingots': 11} == purse
    next_purse = ex00.add_ingot(ex00.get_ingot(ex00.add_ingot(ex00.empty(purse))))
    assert {"gold_ingots": 1} == next_purse


def test_ex001():
    purses = split_booty({"gold_ingots": 3}, {"gold_ingots": 2}, {"apples": 10})
    assert ({"gold_ingots": 1}, {"gold_ingots": 2}, {"gold_ingots": 2}) == purses
    assert len(purses) == 3
    first = purses[0]['gold_ingots']
    second = purses[1]['gold_ingots']
    third = purses[0]['gold_ingots']
    assert second - 1 <= first <= second + 1
    assert third - 1 <= first <= third + 1
    assert third - 1 <= second <= third + 1
