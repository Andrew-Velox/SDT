from person import Teacher,Student
from school import School

class Subject:
    def __init__(self,name,teacher):
        self.name=name
        self.teacher=teacher
        self.max_grade=100
        self.pass_grade=33

    
    def exam(self,students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.subject_marks[self.name] = mark
            student.subject_grade[self.name] = School.calculate_grade(mark) 
        