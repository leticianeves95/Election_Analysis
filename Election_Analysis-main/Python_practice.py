print("Hello World")
counties =["Arapahoe","Denver","Jefferson"]
if counties[1]=='Denver' :
    print(counties[1])

    if "El Paso" in counties:
        print ("El Paso is in the list of counties.")
else:
        print ("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
        print ("Arapahoe or El Paso is in the list of counties")
else:
        print ("Arapahoe and El Paso is not in the list of counties")

for county in counties:
        print(county)

numbers = [0,1,2,3,4]
for num in numbers:
    print(num)


for num in range(5):
    print(num)

for i in range (len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829,"Denver":463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(keys)

for voters in counties_dict:
    print(counties_dict.get(county))

for key, value in counties_dict.items():
    print(key,value)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson","registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.value():
        print(value)

for county,voters in counties_dict.items():
    print(county + county has + str(voters) + "registered voters."

counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has" + str(voters) + " registered voters.")

for county, voters counties_dict.items():
    print(f"{county} county had {voters:,}registered voters.")
    
    voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353}
{"county":"Jefferson","registered_voters": 432438}]

for fish in voting_data:

    county = fish['county']
    voters = fish['registered_voters']

    print(f"{county} county had {voters:,} registered voters.")
    #print(voting_dict)
    #print(fish['county'])


