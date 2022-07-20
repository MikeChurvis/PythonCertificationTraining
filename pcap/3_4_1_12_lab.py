class Timer:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{}:{}".format(
            str(self.hour).rjust(2, '0'),
            str(self.minute).rjust(2, '0'),
            str(self.second).rjust(2, '0'),
        )

    def next_second(self):
        self.second += 1
        self.cycle_timeparts_if_needed()

    def prev_second(self):
        self.second -= 1
        self.cycle_timeparts_if_needed()

    def cycle_timeparts_if_needed(self):
        if not 0 < self.second < 60:
            self.minute += self.second // 60
            self.second %= 60

        if not 0 < self.minute < 60:
            self.hour += self.minute // 60
            self.minute %= 60

        if not 0 < self.hour < 24:
            self.hour %= 24


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
