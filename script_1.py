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
