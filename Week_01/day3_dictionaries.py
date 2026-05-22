# --------------------- Part A -----------------------#

# Dictionary = key:value pairs (like a real dictionary)

student = {
    "name": "Ali",
    "age": 20,
    "grade": 85,
    "city": "Lahore"
}

# Accessing values
print(student["name"])
print(student.get("age"))
print(student.get("grade", "N/A"))

# Adding and Updating

student["email"] = "ali@gmail.com"
student["marks"] = 90
print(student)

# Deleting
del student["city"]
print(student)

# Looping through dictionary
for key, value in student.items():
    print(f"{key}: {value}")
    
# --------------------- Part B (Useful Dictionary Methods) -----------------------#

# All keys, values , items

print(student.keys())
print(student.values())
print(student.items())

# Dictionary comprehension (like list comprehension!)

numbers = [1, 2, 3, 4 ,5]
squared_dict = {n: n**2 for n in numbers}
print(squared_dict)

# Nested dictioray (very common in Ml/APIs)

students = {
    "Ali": {"marks":85, "grade": "B"},
    "Sara": {"marks": 95, "grade": "A"}
}
print(students["Sara"]["grade"])

# --------------------- Part C (Sets)-----------------------#

# Sets = unique values only, no duplicates

fruits = {"apple", "banana", "orange", "apple"}
print(fruits)

# Common use - removing duplicates from a list

numbers = [1,2,2,3,3,3,4]
unique = list(set(numbers))
print(unique)

# Set operations

a = {1,2,3,4}
b = {3,4,5,6}

print(a & b)
print(a | b)
print(a - b)