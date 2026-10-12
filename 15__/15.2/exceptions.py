class GroupOverflowError(Exception):
    """Виняток користувача: у групі не може бути більше 10 студентів."""

    def __init__(self, max_students=10):
        self.max_students = max_students
        super().__init__(f'Група переповнена: максимум {max_students} студентів')
