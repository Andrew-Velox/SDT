import random
from school import School

class Person:
    def __init__(self,name):
        self.name=name
    

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def evaluate_exam(self):
        return random.randint(1,100)
    
class Student(Person):
    def __init__(self, name,classroom):
        super().__init__(name)
        self.classroom=classroom
        self.__id=None
        self.subject_marks={}
        self.subject_grade={}
        self.grade=None
    
    def calculate_final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            sum+=School.grade_to_gpa(grade)
        if sum==0:
            gpa=0.00
        else:
            gpa = sum/len(self.subject_grade)
            self.grade=School.gpa_to_grade(gpa)
        return f"{self.name} Final Grade: {self.grade} With GPA = {gpa}"

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id = value

