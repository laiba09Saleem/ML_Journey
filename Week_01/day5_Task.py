'''1. Create a class called "MLEngineer" with:
   - Attributes: name, skills (list), experience_years
   - Method: introduce() — prints name and years
   - Method: add_skill(skill) — adds to skills list
   - Method: show_skills() — prints all skills neatly
   - Method: is_senior() — returns True if experience > 3'''
   
class MLEngineer:
    
    def __init__(self, name, experience_years):
        self.name = name
        self.skills = []
        self.experience_years = experience_years
        
    def introduce(self):
        print(f"Hi! I'm {self.name}, I have {self.experience_years} years of experience.")
        
    def add_skill(self, skill):
        self.skills.append(skill)
        
    def show_skills(self):
        print(f"{self.name}'s skills:")
        for skill in self.skills:
            print(f"- {skill}")
            
    def is_senior(self):
        return self.experience_years > 3
    
'''2. Create 2 MLEngineer objects with different
   values and call all methods on both'''
   
engineer1 = MLEngineer("Alice", 5)
engineer2 = MLEngineer("Bob", 2)
engineer1.introduce()
engineer1.add_skill("Python")
engineer1.add_skill("TensorFlow")
engineer1.show_skills()
print(f"Is {engineer1.name} a senior? {engineer1.is_senior()}")

engineer2.introduce()
engineer2.add_skill("Scikit-learn")
engineer2.show_skills()
print(f"Is {engineer2.name} a senior? {engineer2.is_senior()}")

'''3. Create a child class "SeniorMLEngineer" that
   inherits from MLEngineer and adds:
   - Attribute: team_size
   - Method: lead_team() — prints who they lead'''
   
class SeniorMLEngineer(MLEngineer):
    
    def __init__(self, name, experience_years, team_size):
        super().__init__(name, experience_years)
        self.team_size = team_size
        
    def lead_team(self):
        print(f"{self.name} leads a team of {self.team_size} engineers.")
        
# Add this and run it
senior = SeniorMLEngineer("Alice", 6, 8)
senior.introduce()        # inherited ✅
senior.add_skill("MLOps") # inherited ✅
senior.show_skills()      # inherited ✅
senior.lead_team()        # new method ✅
print(f"Is senior? {senior.is_senior()}")  # inherited ✅