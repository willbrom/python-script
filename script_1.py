"""
Capitalize each item of a list and update the list
"""
names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc',
         'nigel incubator-jones', 'philip diplodocus mallory']
print(names)

for index in range(len(names)) :
    names[index] = names[index].title()

print(names)


"""
Create Html list
"""
def html_list(str_list):
    start_item_tag = "<li>"
    end_item_tag = "</li>"
    list_body = ""
    for each_str in str_list:
        list_body += start_item_tag + str(each_str) + end_item_tag + "\n"
    return "<ul>\n" + list_body + "</ul>"

print(html_list(["strings", 2.0, True, "and other types too!"]))


"""
Square number
"""
def square_num(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2

print(square_num(89))


"""
Cargo problem
"""
# each item in the manifest is an item and its weight
manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]

def cargo_problem(manifest, weight_limit):
    weight_reached = 0
    for item in manifest:
        if weight_limit >= weight_reached + item[1]:
            weight_reached += item[1]
        else:
            break
    return weight_reached

print(cargo_problem(manifest, 52))


"""
Create String from list exactly 140 char long
"""
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""

for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(len(news_ticker))


"""
Refactor code
"""
# Orignal code
def check_answers(my_answers,answers):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    results= [None, None, None, None, None]
    if my_answers[0] == answers[0]:
        results[0] = True
    elif my_answers[0] != answers[0]:
        results[0] = False
    if my_answers[1] == answers[1]:
        results[1] = True
    elif my_answers[1] != answers[1]:
        results[1] = False
    if my_answers[2] == answers[2]:
        results[2] = True
    elif my_answers[2] != answers[2]:
        results[2] = False
    if my_answers[3] == answers[3]:
        results[3] = True
    elif my_answers[3] != answers[3]:
        results[3] = False
    if my_answers[4] == answers[4]:
        results[4] = True
    elif my_answers[4] != answers[4]:
        results[4] = False
    count_correct = 0
    count_incorrect = 0
    for result in results:
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1
    if count_correct/5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."

print(check_answers(['a', 'a', 'a', 'd', 'e'], ['a', 'b', 'c', 'd', 'e']))

# Refacored code
def check_answers_refactored(my_answers, answers):
    correct_count = 0
    for index in range(len(answers)):
        if  my_answers[index] == answers[index]:
            correct_count += 1
    if correct_count/len(answers) > 0.7:
        return "Congratulations, you passed the test! You scored " + str(correct_count) + " out of " + str(len(answers)) + "."
    else:
        return "Unfortunately, you did not pass. You scored " + str(correct_count) + " out of " + str(len(answers)) + "."

print(check_answers_refactored(['a', 'b', 'c', 'a', 'e', 'f', 'g'], ['a', 'b', 'c', 'd', 'e', 'f', 'g']))
