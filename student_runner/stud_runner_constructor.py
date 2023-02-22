from student_package.Student_module_constructor import Student

#static variable called using class
Student.schoolName="ONGC School"
Student.schoolAddress="Dehradun"


## non static is called using a object

stud1=Student(1001,"Jack","jack@gmail.com",45.2)
stud2=Student(studentRollno=1002,studentName="Peter",studentMailid="peter@gmail.com",studentPercentage=45.)
stud3=Student(1003,"mark","mark@gmail.com",45.)

print(stud1.studentMailid,stud2.studentMailid,stud3.studentMailid)
print(stud1.studentRollno,stud2.studentRollno,stud3.studentRollno)

#stud2.get_student_name()
#to print, assign a variabe and print or print(stud2.get_student_name())

#property
print(stud1.get_name_with_percentage)

res=stud1.get_name_with_percentage()
print (res)

#for non static , we need to give an object like stud1
print(stud1.get_name_with_percentage())
#get_name_with_percentage() is a method and stud1 is object



#for static method, call using Class
print(Student.get_school_detail())
