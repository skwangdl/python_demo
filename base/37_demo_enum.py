from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb'))

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1

if __name__ == '__main__':
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)
    print(Weekday.Sun.value)