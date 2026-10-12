from student import Student
from group import Group
from exceptions import GroupOverflowError

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)  # Only one student

# Перевірка винятку з попереднього ДЗ: спроба додати 11-го студента
gr2 = Group('PD2')
try:
    for i in range(1, 12):
        gr2.add_student(Student('Male', 20, f'Name{i}', f'Surname{i}', f'AN{100 + i}'))
except GroupOverflowError as e:
    print(f'Помилка: {e}')
