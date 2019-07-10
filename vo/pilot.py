from datetime import datetime

from utils.date import RaceDate


class Pilot:

    code = 0
    name = ''
    laps = []

    def __init__(self,
                 code,
                 name,
                 laps,
                 ):
        self.code = code
        self.name = name
        self.laps = laps

    def fastest_lap(self):
        self.laps.sort(key=lambda x: x.lap_time)
        return self.laps[0]

    def total_laps(self):
        return len(self.laps)

    def total_racetime(self):
        time = datetime.strptime('00:00.000', '%M:%S.%f')

        for l in self.laps:
            time = time + RaceDate.convert_to_timedelta(l.lap_time)
        return time.strftime('%M:%S.%f')

    def calculate_speed(self):
        speed = 0
        for l in self.laps:
            speed = speed + float(l.speed.replace(',', '.'))
        return speed / self.total_laps()

    def __str__(self):
        return {'Name': self.name,
                'Best Lap': RaceDate.convert_to_timedelta(self.fastest_lap().lap_time),
                'Race time': self.total_racetime(),
                'Laps': self.total_laps()}
