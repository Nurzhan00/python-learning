from math_utils import add_numbers
from employees import average_salary, employees


def greet(name):
    return f"Привет, {name}! Я учусь Python."


print(greet("Nurzhan"))


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


print(average_salary(employees))


def add_print(a, b):
    print(a + b)


def add_return(a, b):
    return a + b


result = add_print(5, 5)
print(result)  # вот здесь увидишь None

result = add_return(5, 5)
print(result)  # а здесь 10


def get_element(numbers, index):
    # index = 10
    try:
        # print(numbers[10])
        return numbers[index]
    except IndexError:
        # print("None")
        return None


numbers = [1, 2, 3]
print(get_element(numbers, 1))  # должно вернуть 2
print(get_element(numbers, 10))  # должно вернуть None
