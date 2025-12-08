# File I/O:

"""
Docstring for 11_File_I.O.name

File I/O in Python means File Input and Output — basically:

How Python reads from files and writes to files.

Let’s explain it simply and beginner-friendly.

🧠 What is File I/O?

File I/O is about two things:

1️⃣ Input → Reading files

(e.g., reading text from a .txt file)

2️⃣ Output → Writing files

(e.g., saving data to a .txt file)

Why is File I/O important?

Because programs often need to:

read saved data

write user data to a file

log information

read configurations

save game progress

export reports
"""

names = [];

for _ in range(3):
    name = input("Enter name: ");
    names.append(name);


print(names);

##############################################################

name = input("Enter your name: ");
file = open("names.txt", "w");

file.write(name);
file.close();

file_2 = open("names_.txt", "a");

file_2.write(f"{name}\n");
file_2.close();