'''1. Create a dictionary of 5 students with their
   names as keys and marks as values
   Example: {"Ali": 85, "Sara": 92 ...}'''
   
students_marks = {
    "Ali": 85, 
    "Sara": 92,
    "John": 78,
    "Emily": 88,
    "Michael": 90
}
print(students_marks)

'''2. Print only students who scored more than 80
   using a loop'''
        
for student, mark in students_marks.items():
    if mark > 80:
        print(f"{student}: {mark}")
        
'''3. Create a new dictionary using dictionary
   comprehension that shows each student's
   grade: A if marks>=90, B if marks>=80, else C'''
   
student_grades = {student: ('A' if mark >= 90 else 'B' if mark >= 80 else 'C')
                  for student, mark in students_marks.items()}
print(student_grades)

'''4. You have this list with duplicates:
   [1,2,2,3,4,4,4,5,5,6]
   Remove duplicates using a set and
   print the unique sorted values'''

numbers = [1,2,2,3,4,4,4,5,5,6]
unique_numbers = sorted(set(numbers))
print(unique_numbers)
