import numpy as np

def demo_unpack():
    data = ['ACE', 50, 91.1, (2019, 1, 2)]
    a, b, c, d = data
    print(a)
    print(b)
    print(c)
    print(d)
    str = 'kepler'
    e,f,g,h,i,j = str
    print('{} {} {} {} {} {}'.format(e,f,g,h,i,j))

def drop_first_last():
    grades = (100,2,3,4,5,6,80)
    first, *middle, last = grades
    print(np.mean(middle))

if __name__ == '__main__':
    demo_unpack()
    drop_first_last()