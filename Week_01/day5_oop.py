# -------------- Part A — Classes & Objects -------------#

# A class is a blueprint

class Student:
    
    # __init__ runs automatically when object is created
    def __init__(self, name, age, marks):
        self.name = name          # attribute         
        self.age = age          # attribute
        self.marks = marks          # attribute
        
    # Method (function inside a class)
    def introduce(self):
        print(f"Hi! I'm {self.name}, I'm {self.age} years old.")
        
    def get_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        else:
            return 'C'
        
    def study(self, subject):
        print(f"{self.name} is studying {subject}")
        
# Creating objects (instances)
student1 = Student("Ali", 20, 85)
student2 = Student("Sara", 22, 95)

# Using the object

student1.introduce()
print(student1.get_grade())
student2.study("Machine Learning")

# Accessing attributes directly
print(student1.name)
print(student2.marks)

# -------------- Part B — Inheritance -------------#

# Parent class

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def speak(self):
        print(f"{self.name} says {self.sound}")
        
# Child class - inherits from Animal

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof!") # Call parent __init__
        self.tricks = []
        
    def learn_trick(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned {trick}!")
        
    def show_tricks(self):
        print(f"{self.name} knows: {self.tricks}")
        
class Cat(Animal):
    def __init__(self, name):
        super() .__init__(name, "Meow!")
        
    def purr(self):
        print(f"{self.name} is purring...")
        
# Using inheritance
dog = Dog("Bruno")
dog.speak()
dog.learn_trick("sit")
dog.learn_trick("shake")
dog.show_tricks()

cat = Cat("Whiskers")
cat.speak()
cat.purr()

# -------------- Part C — Why OOP Matters in ML -------------#

# This is EXACTLY how Scikit-learn works internally!

class SimpleMLModel:
    
    def __init__(self):
        self.is_trained = False
        self.data = None
        
    def fit(self, data):
        # "Training" the model
        self.data = data
        self.is_trained = True
        print("Model trained successfully!")
        
    def predict(self, input_value):
        if not self.is_trained:
            print("Train the model first!")
            return None
        
        # Simple fake prediction
        avg = sum(self.data) / len(self.data)
        return f"Prediction based on average: {avg: .2f}: {input_value * avg: .2f}"  
    
    def evaluate(self):
        if self.is_trained:
            print(f"Model trained on {len(self.data)} samples.")
            
# This is how we'll use Sciket-learn soon!
model = SimpleMLModel()
model.fit([10, 20, 30, 40, 50])
print(model.predict(2))
model.evaluate()