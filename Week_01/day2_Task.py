'''1. Write a function that takes a list of numbers
   and returns the smallest and largest number'''


def find_min_max(numbers):
    if not numbers:
        return None, None
    min_num = min(numbers)
    max_num = max(numbers)
    return min_num, max_num

numbers = [3, 1, 4, 1, 5, 9]
min_num, max_num = find_min_max(numbers)
print(f"Minimum: {min_num}, Maximum: {max_num}")

''' 2. Write a function that takes a name and age
   and prints: "My name is Ali and I am 20 years old"
   Make age have a default value of 18'''

def print_info(name, age=18):
    print(f"My name is {name} and I'm {age} years old")
    
print_info("Ali", 20)
print_info("Sara")

'''3. Use lambda to filter only even numbers
   from this list: [1,2,3,4,5,6,7,8,9,10]
   Hint: use filter() with lambda'''

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)

'''4. Create a list of 5 students with their marks
   like: [("Ali", 75), ("Sara", 90)...]
   Sort them by marks using lambda (highest first)'''

students = [("Ali", 85), ("Sara", 76), ("Omer", 90), ("Arham", 96), ("Aliya", 70)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)