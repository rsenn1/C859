#7.4.1: Functions: Factoring out a unit-conversion #calculation.
#Write a function so that the main program below can be #replaced by the simpler code that calls function #mph_and_minutes_to_miles(). 

def mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):
    hours_traveled = minutes_traveled / 60.0
    miles_traveled = hours_traveled * miles_per_hour
    return miles_traveled

miles_per_hour = float(input())
minutes_traveled = float(input())

print('Miles: {:f}'.format(mph_and_minutes_to_miles(miles_per_hour, minutes_traveled)))
