dict_ = {
    'Timur': {'history': 90, 'math': 95, 'literature': 91},
    'Olga': {'history': 92, 'math': 96, 'literature': 81},
    'Nik': {'history': 84, 'math': 85, 'literature': 87}
}

new_dict = {student: subject for student, subjects in dict_.items() for subject, grade in subjects.items() if grade == max(subjects.values())}

print(new_dict)
