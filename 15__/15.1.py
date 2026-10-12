class GroupOverflowError(Exception):
    """Виняток користувача: у групі не може бути більше 10 студентів."""

    def __init__(self, max_students=10):
        self.max_students = max_students
        super().__init__(f'Група переповнена: максимум {max_students} студентів')


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.gender}, {self.age}, {self.first_name} {self.last_name}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.gender}, {self.age}, {self.first_name} {self.last_name}, record book: {self.record_book}'


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        # Якщо студента ще немає в групі й місць уже немає, порушуємо виняток
        if student not in self.group and len(self.group) >= self.MAX_STUDENTS:
            raise GroupOverflowError(self.MAX_STUDENTS)
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)

        if student is not None:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

        return None

    def __str__(self):
        all_students = ''

        for student in self.group:
            all_students += str(student) + '\n'

        return f'Number:{self.number}\n {all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

# Перевірка винятку: поза межами класу перехоплюємо спробу додати 11-го студента
gr2 = Group('PD2')
try:
    for i in range(1, 12):  # 11 студентів
        gr2.add_student(Student('Male', 20, f'Name{i}', f'Surname{i}', f'AN{100 + i}'))
        print(f'Додано студента {i}')
except GroupOverflowError as e:
    print(f'Помилка: {e}')

assert len(gr2.group) == 10, 'У групі має бути рівно 10 студентів'