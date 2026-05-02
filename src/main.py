def greet(name):
    return f"Привет, {name}! Я учусь Python."


print(greet("Nurzhan"))


def add_numbers(a, b):
    return a + b


print(add_numbers(5, 5))

age = 25
price = 3.14
name = "Nurzhan"
is_developer = False
skills = ["Python", "Git", "VS Code"]
person = {"name": "Nurzhan", "age": 25}

print(type(age))
print(type(price))
print(type(name))
print(type(is_developer))
print(type(skills))
print(type(person))

age = 15

if age >= 18:
    print("Adult")
elif 13 < age < 18:
    print("Teenager")
else:
    print("Child")


def get_age_category(age):
    if age >= 18:
        return "adult"
    elif 13 < age < 18:
        return "teenager"
    else:
        return "child"


print(get_age_category(25))
print(get_age_category(15))
print(get_age_category(8))

ages = [5, 12, 17, 20, 33, 8, 15]

even = []
odd = []

for age in ages:
    if age % 2 == 0:
        even.append(age)
    else:
        odd.append(age)

print(even)
print(odd)

skills = ["Python", "Git", "Docker"]

for i, skill in enumerate(skills):
    print(i, skill)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = []
odd = []
dictt = {"even": even, "odd": odd}

for age in ages:
    if age % 2 == 0:
        even.append(age)
    else:
        odd.append(age)

print(dictt)


def list_to_dict(numbers):
    even = []
    odd = []
    dictt = {"even": even, "odd": odd}
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return dictt


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_to_dict(numbers))

person = {"name": "Nurzhan", "age": 25, "skills": ["Python", "Git"]}

print(person["name"])
print(person.get("salary", 0))
person["city"] = "Almaty"
print(person)


def average_salary(employees):
    average = 0
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
print(average_salary(employees))
