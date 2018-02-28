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

def get_rating_from_five_scores(score1, score2, score3, score4, score5):
	score1 = int(score1)
	score2 = int(score2)
	score3 = int(score3)
	score4 = int(score4)
	score5 = int(score5)

	required_total_score = remove_outliers(score1, score2, score3, score4, score5)
	average_score = required_total_score / 3

	return get_rating_from_avg_score(average_score)

def remove_outliers(score1, score2, score3, score4, score5):
	total_score = score1 + score2 + score3 + score4 + score5
	total_score_no_outlier = total_score - min(score1, score2, score3, score4, score5) - max(score1, score2, score3, score4, score5)
	return total_score_no_outlier

def get_rating_from_avg_score(average_score):
	if 0 <= average_score < 1:
		return "Terrible"
	elif 1 <= average_score < 2:
		return "Bad"
	elif 2 <= average_score < 3:
		return "OK"
	elif 3 <= average_score < 4:
		return "Good"
	elif 4 <= average_score <= 5:
		return "Excellent"
	else:
		return "Rating not recognized"

score1 = 0
score2 = 1
score3 = 1
score4 = 1
score5 = 5

print(volume)
print(days_to_weeks(10))
print(months_to_years(32))
print("Approx {} months!".format(months_alive(24)))
print("Rating of these scores({}, {}, {}, {}, {}) is: {}".format(score1, score2, score3, score4, score5, get_rating_from_five_scores(score1, score2, score3, score4, score5)))

name_list = ['john', 'mavrik', 'Legend']
name_list_with_line_break = "-".join(name_list)

print(name_list_with_line_break)

for name in name_list:
	print(name.title())
