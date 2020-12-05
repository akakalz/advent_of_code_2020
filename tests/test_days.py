import pytest
from day_01 import Day1
from day_02 import Day2
from day_03 import Day3
from day_04 import Day4


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


@pytest.mark.parametrize(
    "slope,expected_trees", [
        ((1, 1), 38),
        ((2, 2), 19),
        ((3, 3), 12),
        ((4, 4), 9),
        ((5, 5), 7),
        ((1, 3), 2),
        ((1, 5), 2),
        ((1, 7), 2),
        ((2, 1), 1),
    ]
)
def test_day_3_traversal(slope, expected_trees):
    # arrange
    test_obj = Day3('input/day_three_input.txt')
    # act
    actual_trees = test_obj._traverse_slope(slope)
    # assert
    assert actual_trees == expected_trees


def test_day_3():
    # arrange
    test_obj = Day3('input/day_three_input.txt')
    expected_part_1_answer = 2
    expected_part_2_answer = 38 * 2 * 2 * 2 * 1
    # act
    actual_part_1_answer = test_obj.part_1()
    actual_part_2_answer = test_obj.part_2()
    # assert
    assert actual_part_1_answer == expected_part_1_answer
    assert actual_part_2_answer == expected_part_2_answer


def test_day_4():
    # arrange
    test_obj = Day4('input/day_four_input.txt')
    expected_part_1_answer = 8
    expected_part_2_answer = 4
    # act
    actual_part_1_answer = test_obj.part_1()
    actual_part_2_answer = test_obj.part_2()
    # assert
    assert actual_part_1_answer == expected_part_1_answer
    assert actual_part_2_answer == expected_part_2_answer
