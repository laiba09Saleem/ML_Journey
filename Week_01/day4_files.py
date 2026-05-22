# ---------------- Part A — Read & Write Text Files -------------------- #

# Writing a file

with open("notes.txt", "w") as f:
    f.write("Hello this is line 1\n")
    f.write("This is line 2\n")
    f.write("This is line 3\n")
    
# Reading entire file

with open("notes.txt", "r") as f:
    content = f.read()
    print(content)
    
# Reading line by line better for large files

with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())
        
# Appending to existing file

with open("notes.txt", "a") as f:
    f.write("This line was added later\n")

# ---------------- Part B — CSV Files -------------------- #

import csv

# Writing CSV

students = [
    ["Name", "Marks", "Grade"],
    ["Alice", 85, "B"],
    ["Bob", 92, "A"],
    ["Charlie", 78, "C" ]
]

with open("student.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)
    
print("CSV file created!")

# Reading CSV

with open("student.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        
# Reading CSV with DictReader(cleaner!)
with open("student.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} scored {row['Marks']}")
        
# ---------------- Part C — JSON Files -------------------- #

import json

student_data = {
    "name": "Ali",
    "marks": 85,
    "subjects": ["Math", "Science", "English"]
}

# Save to JSON

with open("student.json", "w") as f:
    json.dump(student_data, f, indent=4)
print("JSON saved!")

# Read from json

with open("student.json", "r") as f:
    loaded_data = json.load(f)
    
print(loaded_data["name"])
print(loaded_data["subjects"])