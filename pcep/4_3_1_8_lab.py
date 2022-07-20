def is_year_leap(year):
    # Quadricentennial years are always leap years.
    if year % 400 == 0:
        return True

    # No other centennial year is a leap year.
    if year % 100 == 0:
        return False

    # All other years divisible by four is a leap year.
    if year % 4 == 0:
        return True

    # No other year is a leap year.
    return False


def day_count_by_month(year):
    return [
        31,
        29 if is_year_leap(year) else 28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31,
    ]


def days_in_month(year, month):
    return day_count_by_month(year)[month - 1]


def day_of_year(year, month, day):
    if day > days_in_month(year, month):
        return None

    this_month_index = month - 1
    total_days_in_all_past_months = sum(day_count_by_month(year)[:this_month_index])

    return total_days_in_all_past_months + day
    

print(day_of_year(2000, 12, 31) == 366)
