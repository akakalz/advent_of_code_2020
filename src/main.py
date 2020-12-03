from common import pad_left
from __init__ import days


if __name__ == "__main__":
    for i, Day in enumerate(days, start=1):
        d = Day(f"input/input_puzzle_{pad_left(str(i), 2, '0')}.txt")
        print(f"== {str(d)} ====================")
        print(f"    part 1: {d.part_1()}")
        print(f"    part 2: {d.part_2()}")

    print("FIN")
