class Employee:
    company_name = None  # static variable or class variable
    company_location = None  # static variable or class variable

#constructor
    def __init__(self):
        self.emp_id=None  #non static or instance variable
        self.emp_name=None
        self.emp_salary=None
        self.emp_performance=None

# Call static method.
    @staticmethod
    def print_author_name():
        print("Author Name :","Konika Negi")

    def display_employee_record(self):  #self points to the current object
        print(15 * "-")   # it will print hyphen 15 times
        print("Employee ID:" ,self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Performance: ", self.emp_performance)
        print("Company Name:", Employee.company_name)
        print("Company Location:", Employee.company_location)
        print(35 * "-")

    def calculate_bonus(self):
        print(15 * "-")
        if self.emp_performance=="A":
            print(self.emp_name)
            print(self.emp_salary*10)/100
            self.emp_salary=self.emp_salary+((10/100)*self.emp_salary)
            print(self.emp_salary)
            #update salary with 10%
        elif self.emp_performance=="B":
            print(self.emp_name)
            print(self.emp_salary*5)/100
            self.emp_salary=self.emp_salary+((5/100)*self.emp_salary)
            print(self.emp_salary)
        elif self.emp_performance=="C":
            print(self.emp_name)
            print(self.emp_salary*2)/10
            self.emp_salary=self.emp_salary+((2/100)*self.emp_salary)
            print(self.emp_salary)
        else:
            print(self.emp_name, "No Bonus")
        print(15 * "-")