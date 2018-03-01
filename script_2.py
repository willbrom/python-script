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
