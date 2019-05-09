class Clock(object):
    def __init__(self, hour, minute):
        self.HH = hour + (minute // 60)
        self.HH = self.HH % 24


        self.MM = minute % 60

    def __repr__(self):
        return "{}:{}".format(str(self.HH).zfill(2), str(self.MM).zfill(2))

    def __eq__(self, other):
        return self.HH == other.HH and self.MM == other.MM

    def __add__(self, minutes):
        self.HH += (self.MM + minutes) // 60
        self.HH %= 24

        self.MM += minutes
        self.MM %= 60
        return self

    def __sub__(self, minutes):
        self.HH += (self.MM - minutes) // 60
        self.HH %= 24

        self.MM -= minutes
        self.MM %= 60
        return self
