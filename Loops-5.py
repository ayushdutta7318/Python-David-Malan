# LOOPS:

print("Meow");
print("Meow");
print("Meow");

# 1. While Loop:
print("-----WHILE LOOP---------");

i = 1;
while(i !=4):
    print("meow");
    i+=1;

# backward looping:

print("--------------------------");

y=3;
while(y != 0):
    print("Meow");
    y-= 1;


# 2. FOR LOOPS:
print("--------------FOR LOOPS---------------");

for i in [0,1,2,3]:
    print("Meow");

# but abv is not good idea:
print("-----------------------------------------");

for i in range(0,3):
    print("Meow");

print("-------------------------");
print('meow\n'*3);
print("-----------------------");
# for no blank line
print("Meow\n"*3, end="");

# BREAK AND CONTINUE IN LOOPS:

while True:
    n = int(input("Enter n"));
    if(n>0):
        break;

# print meow using for loop in a function:

print("------------------------------------");

def main():
    meow(3);
    get_number();

def meow(n):
    for _ in range(n):
        print("Meow");

# we can do something more with loops:

def get_number():
    while True:
        n = int(input("Enter number n: "));
        if n > 0:
            return n;#here we can use break in place of return and then use return out of loop.

main();


# Using Loops in Lists:

print("----------------------------");
students = ["ayush","raju", "ranjan"];

for elements in students:
    print(elements);


# also

print("--------------------------------------");

for elements in range(len(students)):
    print(f"{elements+1}: {students[elements]}");

# Using loops with dictionaries:

print("--------------------------------------");

students_house = {
    "house_1": "Ayush",
    "house_2": "Rohan",
    "house_3": "Ravi",
}

print(students_house);

for student in students_house:
    print(student, students_house[student]);

# dictionaries inside of lists:

students_list = [
    {"name": "ayush", "job": "Electronics and Electrical Engineer", "house#": 1,}, {"name": "ranjan", "job": "design engineer", "house#":2}, {"name": "mahesh", "job":"Mechatronics Engineer", "house#":None}
]

for elements in students_list:
    print(elements["name"], elements["job"], elements["house#"], sep=", ");