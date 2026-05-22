'''"Student Management System"
A complete mini app that:

Stores students with name, marks, subject in a class
Calculates grades automatically
Saves all data to a CSV + JSON file
Loads data back from files
Shows a summary report with top student, average marks, pass/fail count
'''

import csv
import json

class Student:
    def __init__(self, name, marks, subject):
        self.name = name
        self.marks = marks
        self.subject = subject
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'
        
class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, marks, subject):
        student = Student(name, marks, subject)
        self.students.append(student)

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Name', 'Marks', 'Subject', 'Grade'])
            for student in self.students:
                writer.writerow([student.name, student.marks, student.subject, student.grade])

    def save_to_json(self, filename):
        with open(filename, 'w') as jsonfile:
            json.dump([student.__dict__ for student in self.students], jsonfile, indent=4)


    def load_from_csv(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            self.students = [Student(row['Name'], int(row['Marks']), row['Subject']) for row in reader]

    def load_from_json(self, filename):
        with open(filename, 'r') as jsonfile:
            data = json.load(jsonfile)
            self.students = [Student(item['name'], item['marks'], item['subject']) for item in data]

    def summary_report(self):
        print("\n--- All Students ---")
        for s in self.students:
         print(f"{s.name} | {s.subject} | {s.marks} | Grade: {s.grade}")
        if not self.students:
            print("No students to show.")
            return
        print("--- Summary ---")
        top_student = max(self.students, key=lambda s: s.marks)
        average_marks = sum(student.marks for student in self.students) / len(self.students)
        pass_count = sum(1 for student in self.students if student.grade != 'F')
        fail_count = len(self.students) - pass_count

        print(f"Top Student: {top_student.name} with {top_student.marks} marks")
        print(f"Average Marks: {average_marks:.2f}")
        print(f"Pass Count: {pass_count}")
        print(f"Fail Count: {fail_count}")
        
# Example usage
if __name__ == "__main__":  
    sms = StudentManagementSystem()
    sms.add_student("Alice", 95, "Math")
    sms.add_student("Bob", 85, "Science")
    sms.add_student("Charlie", 55, "History")

    sms.save_to_csv("students.csv")
    sms.save_to_json("students.json")

    sms.load_from_csv("students.csv")
    sms.summary_report()
    sms.load_from_json("students.json")
    sms.summary_report()   



