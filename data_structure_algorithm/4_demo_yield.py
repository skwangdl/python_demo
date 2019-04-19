
# demo about python yield

def foo():
    print("start ...")
    while True:
        res = yield 4
        print("res: ",res)

def foo_next():
    g = foo()
    print(next(g))
    print("*" * 20)
    print(next(g))

def foo_send():
    g = foo()
    print(next(g))
    print("*" * 20)
    print(g.send(7))

def foo(num):
    print("start ...")
    while num < 10:
        num = num + 1
        yield num

if __name__ == '__main__':
    # foo_next()
    # foo_send()
    t = foo(0)
    for n in t:
        print(n)