class RaceController:
    min_laps = 4
    best_lap = None
    winner = None
    race_result = None

    def __init__(self,
                 pilots
                 ):
        self.pilots = pilots

    def _get_best_lap(self):
        list_laps = []
        for p in self.pilots:
            list_laps.extend(p.laps)

        list_laps.sort(key=lambda l: l.lap_time)
        return list_laps[0]

    def _get_winner(self):
        classified_pilots = list(filter(lambda p: p.total_laps() >= self.min_laps, self.pilots))
        classified_pilots.sort(key=lambda p: p.total_racetime())

        if len(classified_pilots) > 0:
            return classified_pilots[0]

    def calculate_race_result(self):
        classified_pilots = list(filter(lambda p: p.total_laps() == self.min_laps, self.pilots))
        not_classified_pilots = list(filter(lambda p: p.total_laps() < self.min_laps, self.pilots))

        classified_pilots.sort(key=lambda p: p.total_racetime())
        not_classified_pilots.sort(key=lambda p: p.total_racetime())

        classified_pilots.extend(not_classified_pilots)
        position = 0
        race_rlist = []
        for p in classified_pilots:
            race_r = {}
            position = position + 1
            race_r['final_position'] = position
            race_r['pilot_code'] = p.code
            race_r['pilot_name'] = p.name
            race_r['qty_laps'] = p.total_laps()
            race_r['best_lap'] = p.fastest_lap().lap_time
            race_r['medium_speed'] = p.calculate_speed()
            race_r['total_time'] = p.total_racetime()
            race_rlist.append(race_r)

        self.winner = self._get_winner()
        self.best_lap = self._get_best_lap()
        self.race_result = race_rlist

    def asdict(self):
        return {'PILOTS': list(p.name for p in self.pilots),
                'WINNER': self.winner.name if self.winner is not None else "THIS TACE HAS NO WINNER YET",
                'BEST_LAP': {'TIME': self.best_lap.lap_time,
                             'PILOT': self.best_lap.pilot_name
                             },
                'RESULT_RACE': self.race_result}
