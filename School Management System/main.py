from school import School
from person import Student,Teacher
from subject import Subject
from classroom import Classroom

school = School("ABC","Dhaka")

eight=Classroom("Eight")
nine=Classroom("Nine")
ten=Classroom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)


andrew = Student("Andrew",eight)
hamim = Student("Hamim",nine)
tamim = Student("Tamim",ten)
shamim = Student("Shamim",ten)

school.student_addmission(andrew)
school.student_addmission(hamim)
school.student_addmission(tamim)
school.student_addmission(shamim)


soaeb = Teacher("Soaeb")
tanveer = Teacher("Tanveer")
musa = Teacher("Musa")


bangla = Subject("Bangla",soaeb)
biology = Subject("Biology",soaeb)
english = Subject("English",tanveer)
physics = Subject("Physics",musa)


school.add_teacher("Bangla",soaeb)
school.add_teacher("Biology",soaeb)
school.add_teacher("English",tanveer)
school.add_teacher("Physics",musa)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(biology)
nine.add_subject(english)
nine.add_subject(bangla)
nine.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(biology)
ten.add_subject(english)
ten.add_subject(physics)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)