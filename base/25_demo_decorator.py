
def debug(func):
    def wrapper():
        print('[DEBUG]: enter {}()'.format(func.__name__))
        return func()
    return wrapper()

@debug
def say_hello():
    print('say hello')

@debug
def say_goodbye():
    print('say hello')

if __name__ == '__main__':
    say_hello
    say_goodbye