from decorator import decorator
from datetime import datetime

@decorator
def logging(func, *args, **kwargs):
    print("[DEBUG] {}: enter {}()".format(datetime.now(), func.__name__))
    return func(*args, **kwargs)

@logging
def say_hello():
    print("hello kepler")

if __name__ == '__main__':
    say_hello()