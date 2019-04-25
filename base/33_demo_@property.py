
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @birth.getter
    def birth(self):
        return self._birth

    @property
    def age(self):
        return 2015-self._birth

if __name__ == '__main__':
    s = Student()
    s.birth = 2019
    print(s.birth)
    print(s.age)