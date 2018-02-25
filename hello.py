print("Hello Friend!")

def cylinder_volume(height, radius):
	pi = 3.14159
	return height * pi * radius**2

def days_to_weeks(days):
	weeks = days//7
	day = days%7
	return "{} week(s) and {} day(s)".format(weeks, day)

def months_to_years(months):
	years = months//12
	month = months%12
	return "{} year(s) and {} month(s)".format(years, month)

def months_alive(age):
	return age*12

volume = cylinder_volume(10, 3)

print(volume)
print(days_to_weeks(10))
print(months_to_years(32))
print("Approx {} months!".format(months_alive(24)))
