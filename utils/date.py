from datetime import datetime, timedelta


class RaceDate:
    @staticmethod
    def convert_to_timedelta(lap_time):
        time = datetime.strptime(lap_time, '%M:%S.%f').time()
        return timedelta(seconds=time.second,
                         microseconds=time.microsecond,
                         minutes=time.minute)
