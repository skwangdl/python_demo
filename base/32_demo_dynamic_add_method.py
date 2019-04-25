
from types import MethodType

class Student():
    pass

class Student_slots():
    __slots__ = ('name', 'age')

def set_age(self, age):
    self.age = age

def demo_add_method():
    s = Student()
    s.set_age = MethodType(set_age, s)
    s.set_age(26)
    print(s.age)
    ss = Student_slots()
    ss.store = 'temp'
    # store 属性未在 __slots__ 中，不能定义， __slots__ 只对当前类的实例有效，对继承的子类无效
    print(ss.store)

if __name__ == '__main__':
    demo_add_method()