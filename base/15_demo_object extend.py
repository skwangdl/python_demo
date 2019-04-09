# coding=UTF-8

class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(init schoolmember: {})'.format(self.name))

    def tell(self):
        print('Name: "{}", Age: "{}"'.format(self.name, self.age), end="")

class Teacher:
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(init teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{}"'.format(self.salary))

class Student:
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(init teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{}"'.format(self.marks))

if __name__ == '__main__':
    teacher = Teacher('teacher', 40, 4000)
    student = Student('student', 25, 100)
    teacher.tell()
    student.tell()