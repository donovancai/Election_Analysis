counties = ["Arapahoe","Denver","Jefferson"]

for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


for x in counties_dict.values():
    print(x)

for county in list(counties_dict.keys())[1]:
    print(county)

for x in counties_dict:
    print(counties_dict[x])

for county in counties_dict:
    print(counties_dict.get(county))

for x, y in counties_dict.items():
    print(x,y)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
               {"county":"Denver", "registered_voters": 463353},
               {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for x in voting_data:
    print(x['registered_voters'])

for x in voting_data:
    print(x['county'])


for x in voting_data:
    for y in x.values():
        print(y)