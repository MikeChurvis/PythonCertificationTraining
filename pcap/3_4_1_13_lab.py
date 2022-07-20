class WeekDayError(Exception):
    pass


class Weeker:
    weekday_labels = "Mon Tue Wed Thu Fri Sat Sun".split()

    def __init__(self, day):
        if day not in Weeker.weekday_labels:
            raise WeekDayError()

        self.__weekday_ordinal = Weeker.weekday_labels.index(day)

    def __str__(self):
        return Weeker.weekday_labels[self.__weekday_ordinal]

    def add_days(self, n):
        self.__weekday_ordinal += n
        self.cycle_weekday_if_needed()

    def subtract_days(self, n):
        self.__weekday_ordinal -= n
        self.cycle_weekday_if_needed()

    def cycle_weekday_if_needed(self):
        days_in_week = len(self.weekday_labels)

        self.__weekday_ordinal %= days_in_week


try:
    weekday = Weeker("Mon")
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker("Monday")
except WeekDayError:
    print("Sorry, I can't serve your request.")
