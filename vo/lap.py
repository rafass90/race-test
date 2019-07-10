log_regex = r'([\d]{2}.[\d]{2}.[\d]{2}.[\d]{3})\s{2,}([\d]{3}\s?).\s?(\w.\w{2,})\s*(\s\d\s)\s*(\s[\d]:[\d]{2}.[\d]{3}\s)\s*(\d{2},\d{2,})'


class Lap:
    hour = None
    pilot_code = 0
    pilot_name = ''
    lap_number = 0
    lap_time = 0
    speed = 0

    def __init__(self,
                 hour,
                 pilot_code,
                 pilot_name,
                 lap_number,
                 lap_time,
                 speed):

        self.hour = hour.strip()
        self.pilot_code = pilot_code.strip()
        self.pilot_name = pilot_name.strip()
        self.lap_number = lap_number.strip()
        self.lap_time = lap_time.strip()
        self.speed = speed.strip()


def lap_builder(lap_array):
    if lap_array is not None and len(lap_array) == 6:
        return Lap(
            hour=lap_array[0],
            pilot_code=lap_array[1],
            pilot_name=lap_array[2],
            lap_number=lap_array[3],
            lap_time=lap_array[4],
            speed=lap_array[5]
            )
