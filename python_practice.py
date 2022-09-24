# defining list
counties = ["Arapahoe","Denver","Jefferson"]

# formatting membership operators exercise
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# formatting membership operators exercise part 2
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

# formatting membership operators exercise part 3
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

# repetition statements / while loops
for county in counties:
    print(county)

Arapahoe = "Arapahoe"
Denver = "Denver"
Jefferson = "Jefferson"

# first way to write a for loop
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

# second way to write a for loop
for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

# iterate through a dictionary, first define dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# write loop
for counties in counties_dict:
    print(counties)

for county in counties_dict.keys():
    print(counties)

for voters in counties_dict.values():
    print(voters)

for counties in counties_dict:
    print(counties_dict[counties])

for counties in counties_dict:
    print(counties_dict.get(counties))

for counties, voters in counties_dict.items():
    print(counties, "county has", voters, "registered voters.")

    voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

# get values from a list of dictionaries

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# get only the name
for county_dict in voting_data:
    print(county_dict['county'])