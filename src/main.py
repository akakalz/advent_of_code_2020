from day_01 import Day1
from day_02 import Day2
from common import pad_left


days = [Day1, Day2]

if __name__ == "__main__":
    for i, Day in enumerate(days, start=1):
        d = Day(f"input/input_puzzle_{pad_left(str(i), 2, '0')}.txt")
        print(f"== {str(d)} ====================")
        print(f"\tpart 1: {d.part_1()}")
        print(f"\tpart 2: {d.part_2()}")

    print("FIN")
