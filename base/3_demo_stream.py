
# demo calculator in python

def demo_if(flag):
    number = 1
    if flag == number:
        print('number {0}'.format(number))
    elif flag != number:
        print('number {0}'.format(number))

def demo_while(flag):
    number = 1
    temp = 0
    while((flag == number) and (temp != 5)):
        print('number {0}'.format(number))
        temp += 1

def demo_for(flag):
    for i in range(1,flag):
        print(i)

def demo_break(flag):


    demo_while(1)
if __name__ == '__main__':
    demo_if(1)
    demo_for(5)
