import wrapt

def logging(level):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        print("[{}]: enter {}()".format(level, wrapped.__name__))
        return wrapped(*args, **kwargs)
    return wrapper

@logging(level='DEBUG')
def say_hello():
    print("hello kepler")

if __name__ == '__main__':
    say_hello()