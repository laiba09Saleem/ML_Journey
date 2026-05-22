# --------------- Part A ------------------ #
#Basic lists
fruits = ["apple", "banana", "mango"]
print(fruits[0])
print(fruits[1])
print(len(fruits))

#Adding & Removing
fruits.append("orange")
fruits.remove("apple")
print(fruits)

#Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[:-1])
print(numbers[-2:])

# --------------- Part B ------------------ #
# For Loop
students =["Ali", "Sara", "John"]
for student in students:
    print(f"Hello {student}!") 

#Loop with Range
for i in range(1,6):
    print(f"Number: {i}")
    
# While Loop
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1
    
# --------------- Part C ------------------ #
# List Comprehension
#Normal Way

squares = []
for i in range(1,6):
    squares.append(i ** 2)
print(squares)

#List Comprehension way (shorter & cleaner)
squares = [i ** 2 for i in range(1,6)]
print(squares)

# With Condition 
even_numbers = [i for i in range(1, 20) if i%2 == 0]
print(even_numbers)