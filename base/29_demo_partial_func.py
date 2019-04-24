import functools

def demo_functools():
    int2 = functools.partial(int, base=2)
    print(int2('1010101'))

if __name__ == '__main__':
    demo_functools()