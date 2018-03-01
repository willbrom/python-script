from countries import country_list

country_counts = {}
for country in country_list:
    if country not in country_counts:
        country_counts[country] = 1
    else:
        country_counts[country] += 1

print(len(country_counts))
