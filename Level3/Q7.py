students = ["Sam", "Alice", "Mona"]
subjects = ["Commerce", "Science", "Computer"]

# Using for loop
student_subject_dict = {}
for i in range(len(students)):
    student_subject_dict[students[i]] = subjects[i]

print("Using for loop:", student_subject_dict)

# Using dictionary comprehension
student_subject_dict_comprehension = {students[i]: subjects[i] for i in range(len(students))}
print("Using dictionary comprehension:", student_subject_dict_comprehension)
