sports = {
    "Football":[
        {"Name": "John", "Age": 29, "Stats": {"Goals": 5, "Assists": 7, "Points": 11}},
        {"Name": "Logan", "Age": 25, "Stats": {"Goals": 8, "Assists": 3, "Points": 15}}
    ],
     "Basketball": [
         {"Name": "Kyle", "Age": 21, "Stats": {"Goals": 35, "Assists": 20, "Points": 50 }},
         {"Name": "Alex", "Age": 33, "Stats": {"Goals": 62, "Assists": 40, "Points": 46}}
     ],
     "Swimming":[
         {"Name": "Mary", "Age": 18, "Stats": {"Laps": 17, "Assists": 0, "Points": 17}},
         {"Name": "July", "Age": 20, "Stats": {"Laps": 8, "Assists": 2, "Points": 5}}
     ]
}
for sports_club, informations in sports.items():
    print (f"{sports_club}")
    for information in informations:
        print (f"   {information ['Name']}, Age: {information ['Age']} ")
        for skills, rate in information ["Stats"].items():
            print (f"      {skills}: {rate}")
    print ("___\n")



