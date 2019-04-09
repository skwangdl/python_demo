
class Robot:
    population = 0
    def __init__(self, name):
        """init data"""
        self.name = name
        print("(Initializing {})".format(self.name))
        Robot.population += 1

    def die(self):
        """I am die"""
        print("{} is being destoryed".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {} robots working".format(Robot.population))

    def say_hi(self):
        print("Greetings, my masters call me: {}".format(self.name))

    @classmethod
    def how_many(cls):
        print("we have {:d} robots".format(cls.population))

if __name__ == '__main__':
    r1 = Robot('r1')
    r1.say_hi()
    Robot.how_many()
    r2 = Robot('r2')
    r2.say_hi()
    Robot.how_many()
    r1.die()
    r2.die()
    Robot.how_many()
