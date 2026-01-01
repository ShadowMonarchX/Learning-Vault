class Department:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

class College:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

class Student:
    def __init__(self, name, gpa, test_score, extracurricular_score):
        self.name = name
        self.gpa = gpa
        self.test_score = test_score
        self.extracurricular_score = extracurricular_score

def admission_counseling(student, college):
    print(f"Welcome, {student.name}, to the Admission Counseling System for {college.name}!")
    for department in college.departments:
        print(f"\nDepartment: {department.name}")
        print(f"Rank: {department.rank}")
        # Assess student's qualifications and provide recommendations
        total_score = student.gpa + student.test_score + student.extracurricular_score
        if total_score >= department.rank * 10:
            print("You have a good chance of admission to this department!")
        else:
            print("Your chances of admission to this department are low. Consider other options.")

# Input from user
college_name = input("Enter college name: ")
college = College(college_name)

num_departments = int(input("Enter the number of departments: "))
for i in range(num_departments):
    department_name = input(f"Enter name for department {i+1}: ")
    department_rank = int(input(f"Enter rank for department {i+1}: "))
    department = Department(department_name, department_rank)
    college.add_department(department)

student_name = input("Enter student name: ")
student_gpa = float(input("Enter student GPA: "))
student_test_score = int(input("Enter student test score: "))
student_extracurricular_score = int(input("Enter student extracurricular score: "))

student = Student(student_name, student_gpa, student_test_score, student_extracurricular_score)

# Perform admission counseling
admission_counseling(student, college)
