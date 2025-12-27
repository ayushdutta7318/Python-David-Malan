# Classes in Python:

"""
Docstring for Classes_3

🧠 What is a Class in Python?

A class is a blueprint for creating objects.

Think of it like this:

Class → design / template

Object → real thing made from the template

Example in real life:

Class: Car

Objects: your car, my car, a taxi, a bus

All cars have:

color

brand

speed

But each car’s values are different.
"""

# class Student:
#     ... #this means do nothing for now
    
class Student:
    def __init__(self, name, house):
        self.name = name;
        self.house = house;


def main():
    s1 = get_student();
    print(f"{s1.name} from {s1.house}");


def get_student():
    name = input("name: ");
    house = input("house: ");
    student = Student(name, house);
    return student;


if __name__ == "__main__":
    main();
