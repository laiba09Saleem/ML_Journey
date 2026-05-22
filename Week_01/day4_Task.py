'''1. Create a text file called "my_goals.txt"
   and write your 5 ML learning goals in it
   then read it back and print each line
   with a number like:
   "Goal 1: Learn Python"
   "Goal 2: ..."'''

# Writing goals to file
goals = [
    "Learn Python",
    "Understand ML algorithms",
    "Build ML projects",
    "Read ML research papers",
    "Join ML community"
]
with open("my_goals.txt", "w") as f:
    for goal in goals:
        f.write(goal + "\n")

# Reading goals from file
with open("my_goals.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"Goal {i}: {line.strip()}")
        
'''2. Create a CSV file called "cities.csv" with
   columns: City, Country, Population
   Add 5 rows of real data
   Then read it back using DictReader and print:
   "City: Lahore | Country: Pakistan | Population: 14000000"'''
   
import csv
cities = [
    ["City", "Country", "Population"],
    ["Lahore", "Pakistan", 14000000],
    ["New York", "USA", 8000000],
    ["Tokyo", "Japan", 9000000],
    ["London", "UK", 7000000],
    ["Paris", "France", 2000000]
]
with open("cities.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(cities)

# Reading cities from CSV file
with open("cities.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"City: {row['City']} | Country: {row['Country']} | Population: {row['Population']}")
        
'''3. Create a dictionary of your week's study
   log like:
   {"Day1": "Lists and Loops", "Day2": "Functions"...}
   Save it as "study_log.json"
   Then read it back and print each day and topic'''

import json
study_log = {
    "Day1": "Lists and Loops",
    "Day2": "Functions",
    "Day3": "Dictionaries and Sets",
    "Day4": "File Handling - TXT, CSV, JSON",
    "Day5": "OOP Concepts"
}
with open("study_log.json", "w") as f:
    json.dump(study_log, f, indent=4)
# Reading study log from JSON file
with open("study_log.json", "r") as f:
    log = json.load(f)
    for day, topic in log.items():
        print(f"{day}: {topic}")
        
    