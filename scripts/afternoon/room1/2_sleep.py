

"""
# Exercise:
Humans in Europe are expected to live ~81 years.  But they spend a lot that time sleeping--silly humans!
Make a list of how much sleep time each teammate needs to feel rested (per night), then multiply it by the European life expectancy
to get a list of Estimated Sleep Expectancies (in years).

What's the average ESE of your group?
"""

# Raw Data:
sleep_per_night = [9, 8, 6.5, 9]  # e.g. [6.5, 9.2, 8, ...]

# Script (fill in here):
ese_years = []
for hours in sleep_per_night:
    ese = hours*81*365/(24*365)
    ese_years.append(ese)

# Output:
print(ese_years)
