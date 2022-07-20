METERS_PER_MILE = 1609.344
METERS_PER_100KM = 100000
LITRES_PER_GALLON = 3.785411784

def liters_100km_to_miles_gallon(liters_per_100km):
    liters_per_meter = liters_per_100km / 100000
    liters_per_mile = liters_per_meter * METERS_PER_MILE
    gallons_per_mile = liters_per_mile / LITRES_PER_GALLON
    miles_per_gallon = 1 / gallons_per_mile
    return miles_per_gallon

def miles_gallon_to_liters_100km(miles_per_gallon):
    miles_per_liter = miles_per_gallon / LITRES_PER_GALLON
    meters_per_liter = miles_per_liter * METERS_PER_MILE
    liters_per_meter = 1 / meters_per_liter
    liters_per_100km = liters_per_meter * METERS_PER_100KM
    return liters_per_100km
    
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
