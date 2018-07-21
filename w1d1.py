#Variables

seconds_in_minute = 60
minutes_in_hour = 60
hours_in_day = 24
days_in_year = 365
years_in_decade = 10
age_in_years = 40
Andreeas_age = 48618000.0
thirty_two_bit_seconds = 4294967295
sixty_four_bit_seconds = 18446744073709551615


print("How many hours are in a year?")
print(hours_in_day * days_in_year)

print("How many minutes in a decade?")
print(minutes_in_hour * hours_in_day * days_in_year * years_in_decade)

print("How many seconds in my age?")
print(seconds_in_minute * minutes_in_hour * hours_in_day * (days_in_year + age_in_years / 4) * age_in_years)

print("How old is Andreea?")
print(Andreeas_age / seconds_in_minute / minutes_in_hour / hours_in_day / days_in_year)

print("How many days till a 32-bit system times out, if it has an integer overflow bug?")
print(thirty_two_bit_seconds / seconds_in_minute / minutes_in_hour / hours_in_day)

print("How many days till a 64-bit system times out, if it has an integer overflow bug?")
print(sixty_four_bit_seconds / seconds_in_minute / minutes_in_hour / hours_in_day)
