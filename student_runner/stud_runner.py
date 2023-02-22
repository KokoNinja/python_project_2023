from student_package.Student_module import Student

Student.schoolName="ONGC School"
Student.schoolAddress="Dehradun"

stud1=Student()
stud2=Student()
stud3=Student()

#student 1 details
stud1.studentRollno="1001"
stud1.schoolName="Jack"
stud1.studentMailid='jack@gmail.com'
stud1.studentPercentage="45.2"

#student 2 details
stud2.studentRollno="1002"
stud2.schoolName="peter"
stud2.studentMailid='peter@gmail.com'
stud2.studentPercentage="85.2"

#student 3 details
stud3.studentRollno="1003"
stud3.schoolName="mark"
stud3.studentMailid='markk@gmail.com'
stud3.studentPercentage="56.5"

stud2=stud1

print(stud1.studentMailid,stud2.studentMailid,stud3.studentMailid)