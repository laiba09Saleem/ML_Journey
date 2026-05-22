# --------------- Part A ------------------ #
# Basic Functions

def greet(name):
    print(f"Hello, {name}!")
greet("Ali")

# Function with return
def add_numbers(a,b):
    return a+b

result = add_numbers(5, 3)
print(result)

# Funtion with default value
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
    
greet("Sara")
greet("Sara", "Hi")

# --------------- Part B ------------------ #
# Multiple Return Values

# Functions can return multiple values
def get_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    return total, average, maximum

scores = [80, 90, 75, 95, 85]
total, avg, high = get_stats(scores)
print(f"Total: {total}, Average: {avg}, Highest: {high}")

# --------------- Part C ------------------ #
#Lambda Functions
# Normal Function

def square(x):
    return x ** 2

#samething as lambda

square = lambda x: x ** 2
print(square(5))

# Lambda with 2 variables

multiply = lambda a, b: a * b
print(multiply(3, 4))

students = [("Ali", 85), ("Sara", 67)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)