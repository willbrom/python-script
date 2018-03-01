"""
Country problem
"""
from countries import country_list

country_counts = {}
for country in country_list:
    if country not in country_counts:
        country_counts[country] = 1
    else:
        country_counts[country] += 1

print(len(country_counts))



"""
Albums problem
"""
def most_prolific(album_dict):
    year = {}
    for album in album_dict:
        album_year = album_dict[album]
        if album_year not in year:
            year[album_year] = 1
        else:
            year[album_year] += 1

    year_count = []
    for year_key in year:
        year_count.append(year[year_key])

    max_num = max(year_count)
    for year_key in year:
        if year[year_key] == max_num:
            return year_key

Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964, "Lollipop": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

dicc = {'Rubber Soul': 1965, 'Magical Mystery Tour': 1967, "Sgt. Pepper's Lonely Hearts Club Band": 1967, 'Revolver': 1966,
 'The Beatles': 1968, 'With the Beatles': 1963, 'Beatles for Sale': 1964,
 'Yellow Submarine': 1969, "A Hard Day's Night": 1964, 'Help': 1965,
 'Let It Be': 1970, 'Abbey Road': 1969,
 'Twist and Shout': 1964, 'Please Please Me': 1963}
# 1964
print(most_prolific(Beatles_Discography))
print(most_prolific(dicc))



"""
Circus problem
"""
def total_takings(monthly_takings):
    total_takings = 0
    for month in monthly_takings:
        takings = monthly_takings[month]
        for taking in takings:
            total_takings += taking
    return total_takings

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}

print(total_takings(monthly_takings))



"""
Refactored Circus problem
"""
def total_takings_ref(monthly_takings):
    #total is used to sum up the monthly takings
    total = 0
    for month in monthly_takings.keys():
        #I use the Python function sum to sum up over
        #all the elements in a list
        total = total + sum(monthly_takings[month])
    return total
