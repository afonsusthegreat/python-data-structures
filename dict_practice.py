student = {
    'name': 'Joãozinho',
    'age': 18
}
print(student)
print(student.get('name'))
print(student.get('course', 'Não tem curso'))

student['course'] = 'CC'

if 'age' in student:
    print('Joãozinho tem', student.get('age'), 'anos')
