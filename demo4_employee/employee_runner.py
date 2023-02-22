# to call static variable, call the class name

from demo4_employee.employee_module import Employee

Employee.company_name = "iFuture"
Employee.company_location = "Pune"

print(Employee.company_name)
print(Employee.company_location)

#creating object
emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

emp1.emp_id = 100
emp1.emp_name = "Loki"
emp1.emp_salary = 5000
emp1.emp_performance = "A"

emp2.emp_id = 101
emp2.emp_name = "Thor"
emp2.emp_salary = 60000
emp2.emp_performance = "B"

# load employee details in emp3
emp3.emp_id = 102
emp3.emp_name = "Hulk"
emp3.emp_salary = 60000
emp3.emp_performance = "C"

print(emp1.emp_id, emp1.emp_name,emp1.emp_salary,emp1.emp_performance)
print(emp2.emp_id, emp2.emp_name,emp2.emp_salary,emp2.emp_performance)
print(emp3.emp_id, emp3.emp_name,emp3.emp_salary,emp3.emp_performance)


Employee.print_author_name()

emp1.display_employee_record()
emp2.display_employee_record()
emp3.display_employee_record()

emp1.calculate_bonus()
emp2.calculate_bonus()
emp3.calculate_bonus()