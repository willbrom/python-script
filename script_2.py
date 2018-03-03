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



"""
Tuple example
"""
def hours2days(hours):
     days = hours//24
     hour = hours%24
     return days, hour

print(hours2days(10000))



"""
Default args
"""
def print_list(l, numbered=False, bullet_character='-'):
    """Prints a list on multiple lines, with numbers or bullets

    Arguments:
    l: The list to print
    numbered: set to True to print a numbered list
    bullet_character: The symbol placed before each list element. This is
                      ignored if numbered is True.
    """
    for index, element in enumerate(l):
        if numbered:
            print("{}: {}".format(index+1, element))
        else:
            print("{} {}".format(bullet_character, element))

print_list(["cats", "in", "space"])



"""
Create list from txt file

['Graham Chapman', 'Eric Idle', 'Terry Jones', 'Michael Palin', 'Terry Gilliam', 'John Cleese', 'Carol Cleveland', 'Ian Davidson',
'John Hughman', 'The Fred Tomlinson Singers', 'Connie Booth', 'Bob Raymond', 'Lyn Ashley', 'Rita Davies', 'Stanley Mason', 'David Ballantyne',
'Donna Reading', 'Peter Brett', 'Maureen Flanagan', 'Katya Wyeth', 'Frank Lester', 'Neil Innes', 'Dick Vosburgh', 'Sandra Richards',
'Julia Breck', 'Nicki Howorth', 'Jimmy Hill', 'Barry Cryer', 'Jeannette Wild', 'Marjorie Wilde', 'Marie Anderson', 'Caron Gardner',
'Nosher Powell', 'Carolae Donoghue', 'Vincent Wong', 'Helena Clayton', 'Nigel Jones', 'Roy Gunson', 'Daphne Davey', 'Stenson Falke',
'Alexander Curry', 'Frank Williams', 'Ralph Wood', 'Rosalind Bailey', 'Marion Mould', 'Sheila Sands', 'Richard Baker', 'Douglas Adams',
'Ewa Aulin', 'Reginald Bosanquet', 'Barbara Lindley', 'Roy Brent', 'Jonas Card', 'Tony Christopher', 'Beulah Hughes', 'Peter Kodak', 'Lulu',
'Jay Neill', 'Graham Skidmore', 'Ringo Starr', 'Fred Tomlinson', 'David Hamilton', 'Suzy Mandel', 'Peter Woods']
"""
def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename) as f:
        for line in f:
            cast_list.append(line.strip())

    for index in range(len(cast_list)):
        cast = cast_list[index].split(',')
        cast_list[index] = cast[0]

    return cast_list

print(create_cast_list('txt files/flying_circus_cast.txt'))
