class TimeInterval:
    def __init__(self, *, hours=0, minutes=0, seconds=0):
        if any(map(lambda timepart: not isinstance(timepart, int), (hours, minutes, seconds))):
            raise TypeError('All time-parts must be integers.')

        if any(map(lambda timepart: timepart < 0, (hours, minutes, seconds))):
            raise ValueError('All time-parts must be greater than or equal to 0.')

        self.__total_seconds = seconds + minutes * 60 + hours * 3600

    @property
    def total_seconds(self):
        return self.__total_seconds

    @property
    def seconds(self):
        return self.__total_seconds % 60

    @property
    def minutes(self):
        return (self.__total_seconds // 60) % 60

    @property
    def hours(self):
        return self.__total_seconds // 3600

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def __add__(self, other):
        if isinstance(other, TimeInterval):
            return TimeInterval(seconds=self.__total_seconds + other.__total_seconds)

        raise TypeError(f"Addition between {type(self)} and {type(other)} is not supported.")

    def __sub__(self, other):
        if isinstance(other, TimeInterval):
            if self.__total_seconds - other.__total_seconds < 0:
                raise ValueError('Subtraction would result in a negative TimeInterval, which is not supported.')

            return TimeInterval(seconds=self.__total_seconds - other.__total_seconds)

        raise TypeError(f"Subtraction between {type(self)} and {type(other)} is not supported.")

    def __mul__(self, other):
        if isinstance(other, int):
            return TimeInterval(seconds=self.__total_seconds * other)

        raise TypeError(f"Multiplication between {type(self)} and {type(other)} is not supported.")

    def __eq__(self, other):
        if not isinstance(other, TimeInterval):
            return False

        return self.__total_seconds == other.__total_seconds


if __name__ == '__main__':
    def main():
        time_interval_1 = TimeInterval(hours=21, minutes=58, seconds=50)
        time_interval_2 = TimeInterval(hours=1, minutes=45, seconds=22)

        print(time_interval_1, time_interval_2)

        assert time_interval_1 + time_interval_2 == TimeInterval(hours=23, minutes=44, seconds=12)
        assert time_interval_1 - time_interval_2 == TimeInterval(hours=20, minutes=13, seconds=28)
        assert time_interval_1 * 2 == TimeInterval(hours=43, minutes=57, seconds=40)


    main()
