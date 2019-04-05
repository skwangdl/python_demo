
# demo about function
x = 50;
def func(x):
    print('x is', x)
    x = 2
    print('Change local x to ', x)

def func_global():
    global x
    print('x is', x)
    x = 3
    print('change global x is', x)


if __name__ == '__main__':
    func(x)
    print('x is still', x)
    func_global()
    print('change global x is', x)
