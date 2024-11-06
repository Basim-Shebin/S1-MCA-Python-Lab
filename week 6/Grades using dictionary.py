student = {}
student['name'] = input("Enter student's name: ")
student['roll_no'] = input("Enter roll number: ")
student['reg_no'] = input("Enter registration number: ")
student['department'] = input("Enter department: ")
student['semester'] = input("Enter semester: ")
student['total_marks'] = float(input("Enter total marks: "))
if student['total_marks'] >= 90:
    student['grade'] = 'A'
elif student['total_marks'] >= 82:
    student['grade'] = 'B'
elif student['total_marks'] >= 75:
    student['grade'] = 'C'
elif student['total_marks'] >= 60:
    student['grade'] = 'D'
elif student['total_marks'] >= 50:
    student['grade'] = 'P'
else:
    student['grade'] = 'F'

print("\nStudent Details:")
for i, value in student.items():
    print(f"{i}: {value}")
del student['roll_no']

print("\nUpdated Student Details (after deleting roll number):")
for i, value in student.items():
    print(f"{i}: {value}")
