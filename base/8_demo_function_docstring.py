
def print_max(x, y):
    "this is demo about print_max __doc__"
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

if __name__ == '__main__':
    print_max(10,20)
    print(print_max.__doc__)