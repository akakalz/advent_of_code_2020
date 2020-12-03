# import pytest
from day_01 import Day1
from day_02 import Day2


def test_day_1():
    # arrange
    test_obj = Day1('input/day_one_input.txt')
    expected_part_1_answer = 555 * 1465
    expected_part_2_answer = 555 * 1462 * 3
    # act
    actual_part_1_answer = test_obj.part_1()
    actual_part_2_answer = test_obj.part_2()
    # assert
    assert actual_part_1_answer == expected_part_1_answer
    assert actual_part_2_answer == expected_part_2_answer


def test_day_2():
    # arrange
    test_obj = Day2('input/day_two_input.txt')
    expected_part_1_answer = 2
    expected_part_2_answer = 1
    # act
    actual_part_1_answer = test_obj.part_1()
    actual_part_2_answer = test_obj.part_2()
    # assert
    assert actual_part_1_answer == expected_part_1_answer
    assert actual_part_2_answer == expected_part_2_answer
