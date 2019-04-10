
# TODO
class logging(object):
    def __init__(self, level):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(level=self.level, func=func.__name__))
            func(*args, **kwargs)
        return wrapper

@logging(level='DEBUG')
def say_hello(str):
    print('say hello {}'.format(str))

@logging(level='INFO')
def say_goodbye(str):
    print('say goodbye {}'.format(str))

if __name__ == '__main__':
    say_hello('kepler')
    say_goodbye('wsk')