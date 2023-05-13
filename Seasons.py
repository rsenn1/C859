#5.15 LAB: Seasons
#Write a program that takes a date as input and outputs the date's season. The input is a string to represent the month and an int to represent the day.

input_month = input()
input_day = int(input())
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
special = ['April', 'June', 'September', 'November']
if input_month not in months or input_day > 31 or input_day < 1:
    season = "Invalid"
elif input_month in special and input_day == 31:
    season = "Invalid"
else:
    
    if (input_month == 'April') or (input_month == 'May'):
        season = "Spring"
    if (input_month == 'June') and (input_day > 20):
        season = "Summer"
    if (input_month == 'June') and (input_day <= 20):
         season = "Spring"
    if (input_month == 'July') or (input_month == 'August'):
         season = "Summer"
    if (input_month == 'September') and (input_day > 20):
         season = "Autumn"
    if (input_month == 'September') and (input_day <= 20):
        season = "Summer"
    if (input_month == 'October') or (input_month == 'November'):
        season = "Autumn"
    if (input_month == 'December') and (input_day > 20):
        season = "Winter" 
    if (input_month == 'December') and (input_day <= 20):
        season = "Autumn"
    if ((input_month == 'January') or (input_month == 'February')) and input_day > 20:
        season = "Winter"
    if (input_month == 'March') and (input_day > 20):
        season = "Spring"
    if (input_month == 'March') and (input_day <= 20):
        season = "Winter"
print(season)
