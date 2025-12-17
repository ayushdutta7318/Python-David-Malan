# map contd:

students = [
    {"name": "ayush", "house": "house 3"},
    {"name": "ramesh", "house": "house 2"},
    {"name": "suresh", "house": "house 1"},
    {"name": "khushboo", "house": "house 3"},
    {"name": "akanksha", "house": "house 3"},
]

house_3 = [
    student["name"] for student in students if student["house"] == "house 3"
];

print(house_3);