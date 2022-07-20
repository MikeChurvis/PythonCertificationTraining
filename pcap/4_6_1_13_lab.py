"""
Your task is to extend its functionality with a new method called 
count_weekday_in_year, which takes a year and a weekday as parameters, 
and then returns the number of occurrences of a specific weekday in the year.

Use the following tips:

Create a class called MyCalendar that extends the Calendar class;
create the count_weekday_in_year method with the year and weekday parameters. 
The weekday parameter should be a value between 0-6, where 0 is Monday and 
6 is Sunday. The method should return the number of days as an integer;
in your implementation, use the monthdays2calendar method of the Calendar class.
The following are the expected results:

Sample arguments

year=2019, weekday=0

Expected output

52


Sample arguments

year=2000, weekday=6

Expected output

53
"""

import calendar


class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        if year not in range(1, 10000):
            raise ValueError("Invalid year (expects int between 1 and 9999 inclusive)")

        if weekday not in range(7):
            raise ValueError(
                "Invalid weekday (expects int between 0 and 6 inclusive, "
                "where 0 is Monday, ..., and 6 is Sunday)."
            )

        weekdays_in_year = 0

        for month in range(1, 13):
            monthdays = self.monthdays2calendar(year, month)
            for week in monthdays:
                weekday_falls_in_current_month = bool(week[weekday][0])

                if weekday_falls_in_current_month:
                    weekdays_in_year += 1

        return weekdays_in_year


if __name__ == "__main__":

    def main():
        my_calendar = MyCalendar()
        print(
            "Year = 2019, weekday = 0; expect: 52, actual:",
            my_calendar.count_weekday_in_year(2019, 0),
        )
        print(
            "Year = 2000, weekday = 6; expect: 53, actual:",
            my_calendar.count_weekday_in_year(2000, 6),
        )

    main()
