
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must int')
        if value < 0 or value > 100:
            raise ValueError('score must >= 0 and <= 100')
        self._score = value

if __name__ == '__main__':
    s = Student()
    s.score = 10
    print(s.score)
    # 使用@score.setter 在创建实例时，检查输入参数是否符合要求
    s.score = 101
    print(s.score)