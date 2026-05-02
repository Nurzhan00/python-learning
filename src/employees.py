def average_salary(employees):
    # average = 0
    sum_of_salary = 0
    for employee in employees:
        sum_of_salary += employee.get("salary")

    average = sum_of_salary / len(employees)

    employees_v2 = []

    for employee in employees:
        if employee.get("salary") > average:
            employees_v2.append(employee)
        else:
            continue
    return employees_v2


employees = [
    {"name": "Aibek", "salary": 150000},
    {"name": "Dana", "salary": 280000},
    {"name": "Nurzhan", "salary": 320000},
    {"name": "Marat", "salary": 95000},
    {"name": "Aliya", "salary": 210000},
]
