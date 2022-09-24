from itertools import count

counties = ["Arapahoe", "Denver", "Jefferson"]

counties_tuple = ("Arapahoe", "Denver", "Jefferson")

print(len(counties_tuple))

print(counties_tuple)

print(counties_tuple[0:2])
print(counties_tuple[:2])
print(counties_tuple[:-1])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
print(counties_dict)

print(counties_dict.keys())
print(counties_dict.values())

print(counties_dict["Arapahoe"])

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)

# Step 1
voting_data.insert(1, {"county":"El Paso", "registered_voters": 461149})
print(voting_data)

# Step 2
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)

# Step 3
voting_data.remove({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Denver", "registered_voters": 463353})
print(voting_data)

# Step 4
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)
