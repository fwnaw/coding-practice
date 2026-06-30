students = [
    {"name": "Ali", "score": 78},
    {"name": "Sara", "score": 92},
    {"name": "James", "score": 65},
    {"name": "Priya", "score": 88},
    {"name": "Naw", "score": 95}
]

highest = students[0]
for student in students:
    if student['score'] > highest['score']:
        highest = student
print(f"{highest['name']} scored the highest with a score of {highest['score']}")
    
    
total = 0
for student in students:
    total = total + student['score']
print(f"mean score = {total / len(students)}")

for student in students:
    if student['score'] > 80:
        print(f"{student['name']} Pass")
    else:
        print(f"{student['name']} Fail")


