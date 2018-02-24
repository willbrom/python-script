print("Hello World")

def cylinder_volume(height, radius):
	pi = 3.14159
	return height * pi * radius**2

volume = cylinder_volume(10, 3)
print(volume)

def days_to_weeks(days):
	weeks = days//7
	day = days%7
	return "{} week(s) and {} day(s)".format(weeks, day)

print(days_to_weeks(10))
