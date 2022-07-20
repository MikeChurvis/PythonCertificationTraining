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
    
    

def days_in_month(year, month):
    day_count_by_month = [
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
    
    return day_count_by_month[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
