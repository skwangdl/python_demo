class person:
    def __init__(self, name):
        self.name = 'kepler'

    def say_hello(self):
        print('hello kepler, name is ', self.name)

if __name__ == '__main__':
    p = person('kepler')
    p.say_hello()