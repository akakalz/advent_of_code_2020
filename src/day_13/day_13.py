# https://adventofcode.com/2020/day/13

from day import Day


class Day13(Day):
    def __init__(self, file_name: str):
        super().__init__(13, file_name)

    def part_1(self):
        timestamp = int(self.input_data[0])
        bus_lines = {x: dict(loop_minutes=int(x))
                     for x in self.input_data[1].split(",") if x != "x"}
        self.calculate_times(bus_lines, timestamp)
        min_busline = None
        min_board_time = 999999999999999999
        for bus_line in bus_lines:
            if bus_lines[bus_line]["pick_up"] < min_board_time:
                min_busline = bus_line
                min_board_time = bus_lines[bus_line]["pick_up"]
        return bus_lines[min_busline]["loop_minutes"] * \
            bus_lines[min_busline]["wait"]

    def part_2(self):
        bus_lines = [int(x) if x != 'x' else x
                     for x in self.input_data[1].split(",")]
        valid_bus_lines = {
            x: {'index': i} for i, x in enumerate(bus_lines) if x != 'x'
        }
        step = 1
        base_bus = bus_lines[0]
        timestamp = base_bus
        # iterate through buses
        for bus_id in valid_bus_lines:
            index = valid_bus_lines[bus_id]['index']
            # check to see if bus is departing at its correct time
            while (timestamp + index) % bus_id != 0:
                timestamp += step
            # increase step by the previous multiples
            # to find next timestamp for next bus
            step *= bus_id
        return timestamp

    @staticmethod
    def calculate_times(bus_lines, timestamp):
        for key in bus_lines:
            bus_dict = bus_lines.get(key)
            divisor = (timestamp // bus_dict.get("loop_minutes")) + 1
            bus_dict["wait"] = (
                bus_dict.get("loop_minutes") * divisor -
                timestamp
            )
            bus_dict["pick_up"] = bus_dict.get("loop_minutes") * divisor
