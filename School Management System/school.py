class School:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.teachers={}
        self.classrooms={}
    
    def add_classroom(self,classroom):
        self.classrooms[classroom.name]=classroom
    
    def add_teacher(self,subject,teacher):
        self.teachers[subject]=teacher
    
    def student_addmission(self,student):
        classname=student.classroom.name
        self.classrooms[classname].add_student(student)
        
    
    @staticmethod
    def calculate_grade(marks):
        if marks>=80 and marks<=100:
            return "A+"
        elif marks>=70 and marks<80:
            return "A"
        elif marks>=60 and marks<70:
            return "A-"
        elif marks>=50 and marks<60:
            return "B"
        elif marks>=40 and marks<50:
            return "C"
        elif marks>=33 and marks<40:
            return "D"
        else:
            return "F"
    
    @staticmethod
    def grade_to_gpa(grade):
        grade_map={
            "A+": 5.00,
            "A": 4.00,
            "A-": 3.70,
            "B": 3.00,
            "C": 2.00,
            "D": 1.00,
            "F": 0.00
        }
        return grade_map[grade];
    @staticmethod
    def gpa_to_grade(gpa):
        if gpa>4.00 and gpa<=5.00:
            return "A+"
        elif gpa>3.70 and gpa<=4.00:
            return "A"
        elif gpa>3.00 and gpa<=3.70:
            return "A-"
        elif gpa>2.00 and gpa<=3.00:
            return "B"
        elif gpa>1.00 and gpa<=2.00:
            return "C"
        elif gpa>0.00 and gpa<=1.00:
            return "D"
        else:
            return "F"
    
    def __repr__(self):
        for key in self.classrooms.keys():
            print(key)
        

        print("All Students")
        result = "";
        for key,value in self.classrooms.items():
            result+=f"---{key.upper()} Classroom Students\n"
            for student in value.students:
                result+=f"{student.name}\n"

        print(result)


        subject=""
        for key,value in self.classrooms.items():
            subject+=f"---{key.upper()} Classroom Subject\n"
            for sub in value.subjects:
                subject+=f"{sub.name}\n"
        
        print(subject)

        #all teachers
        print("----All Teachers----")
        teach=""
        for key,value in self.teachers.items():
            teach+=f"{key} : {value.name}\n"
        print(teach)
        

        print("----Students Results----")
        for key,value in self.classrooms.items():
            for student in value.students:
                for k,i in student.subject_marks.items():
                    print(student.name,k,i,student.subject_grade[k])
                print(student.calculate_final_grade())


        return ""

