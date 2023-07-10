def max_salary_employee(employees):
    max_salary=0
    max_employee={}

    for employee in employees:
         salary=
         employee.get('salary',0)
         if salary>max_salary:
            max_salary=salary
            max_employee=employee
    
    return max_employee