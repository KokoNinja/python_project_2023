#check changes
class Student:
    schoolAddress = None
    schoolName = None
    __schoolTest=100  ## protected. Cannot be accessed out of the class.

    def __init__(self, studentRollno, studentName, studentMailid, studentPercentage):
        self.studentRollno = studentRollno
        self.studentName = studentName
        self.studentMailid = studentMailid
        self.studentPercentage = studentPercentage
        self.__schoolID=0

    def get_schoolID(self,schoolId):
        return self.__schoolID

    def set_schoolId(self,schoolID):
        if schoolID>100:
            self.__schoolID=schoolID
        else:
            ("Invalid ID")

    # OR
# def __init__(self,studentRollno=NOne,studentName=NOne,studentMailid=NOne,studentPercentage):

# how to check if its optinal or not
# def __init__(self,studentRollno,studentName,studentMailid,studentPercentage):
# Check initi value

#non static method
    def get_student_name(self):
        return self.studentName

#create a non static method to print Hi Jack you rpercentage is 45.2

    @property
    def get_name_with_percentage(self):
        return "HI " + str(self.studentName) + " your percentage is " + str(self.studentPercentage)

    @staticmethod
    def get_school_detail():
        return Student.get_school_detail() + "is located at " + Student.schoolAddress
