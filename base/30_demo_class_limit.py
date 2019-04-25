
class Student():
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s'.format(self.__name, self.__score))

    def get_score(self):
        return self.__score

    def get_name(self):
        return self.__name

if __name__ == '__main__':
    bart = Student('bart', 10)
    bart.__name = 'kepler'
    print(bart.__name)
    print(bart._Student__name)