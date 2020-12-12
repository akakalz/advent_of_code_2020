import pytest
from day_01 import Day1
from day_02 import Day2
from day_03 import Day3
from day_04 import Day4
from day_05 import Day5
from day_06 import Day6
from day_07 import Day7
from day_08 import Day8
from day_09 import Day9
from day_10 import Day10


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


@pytest.mark.parametrize(
    "line,expected_id", [
        (['FFFBFFFRRL'], 8 * 8 + 6),
        (['FFFBBBFLLL'], 14 * 8 + 0),
        (['BFFFBFBRLR'], 69 * 8 + 5),
    ]
)
def test_day_5_row_col_parsing(line, expected_id, generic_input_file):
    # arrange
    test_obj = Day5(generic_input_file)
    test_obj.input_data = line  # replace the data with out own
    # act
    expected_part_1_answer = expected_id
    # act
    actual_part_1_answer = test_obj.part_1()
    # assert
    assert actual_part_1_answer == expected_part_1_answer


@pytest.mark.parametrize(
    "input_data,expected_count", [
        (['ab', '', 'abc', ''], 5),
        (['ab', 'abcd', 'abc', ''], 4),
        (['ab', '', 'abc', 'ab', '', 'ef', 'eg', ''], 8),
    ]
)
def test_day_6_part_1(input_data, expected_count, generic_input_file):
    # arrange
    test_obj = Day6(generic_input_file)
    test_obj.input_data = input_data
    # act
    actual_count = test_obj.part_1()
    # assert
    assert actual_count == expected_count


@pytest.mark.parametrize(
    "input_data,expected_count", [
        (['ab', '', 'abc', ''], 5),
        (['ab', 'abcd', 'abc', ''], 2),
        (['ab', '', 'abc', 'ab', '', 'ef', 'eg', ''], 5),
    ]
)
def test_day_6_part_2(input_data, expected_count, generic_input_file):
    # arrange
    test_obj = Day6(generic_input_file)
    test_obj.input_data = input_data
    # act
    actual_count = test_obj.part_2()
    # assert
    assert actual_count == expected_count


def test_day_7():
    # arrange
    test_obj = Day7('input/day_seven_input.txt')
    expected_part_1_answer = 5
    expected_part_2_answer = 126
    # act
    actual_part_1_answer = test_obj.part_1()
    actual_part_2_answer = test_obj.part_2()
    # assert
    assert actual_part_1_answer == expected_part_1_answer
    assert actual_part_2_answer == expected_part_2_answer


def test_day_8():
    # arrange
    test_obj = Day8('input/day_eight_input.txt')
    expected_part_1_answer = 5
    expected_part_2_answer = 8
    # act
    actual_part_1_answer = test_obj.part_1()
    actual_part_2_answer = test_obj.part_2()
    # assert
    assert actual_part_1_answer == expected_part_1_answer
    assert actual_part_2_answer == expected_part_2_answer


def test_day_9(generic_input_file):
    # arrange
    test_obj = Day9('input/day_nine_input.txt')
    test_obj.part_1_preamble = 5
    expected_part_1_answer = 127
    expected_part_2_answer = 62
    # act
    actual_part_1_answer = test_obj.part_1()
    actual_part_2_answer = test_obj.part_2()
    # assert
    assert actual_part_1_answer == expected_part_1_answer
    assert actual_part_2_answer == expected_part_2_answer


def test_day_10():
    # arrange
    test_obj = Day10('input/day_ten_input.txt')
    expected_part_1_answer = 220
    expected_part_2_answer = 19208
    # act
    actual_part_1_answer = test_obj.part_1()
    actual_part_2_answer = test_obj.part_2()
    # assert
    assert actual_part_1_answer == expected_part_1_answer
    assert actual_part_2_answer == expected_part_2_answer
