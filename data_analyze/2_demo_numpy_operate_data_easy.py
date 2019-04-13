import numpy as np

def print_version():
    print(np.__version__)

def create_array():
    arr = np.arange(10)
    print(arr)

def create_array_all_true():
    arr = np.ones((3,3), dtype=bool)
    print(arr)

def get_odd_number():
    arr = np.array([0,1,2,3,4,5,6,7,8,9])
    arr = arr[arr % 2 == 1]
    print(arr)

def np_where_demo():
    arr = np.array([1,2,3,4,5,6,7,8,9,10])
    out = np.where(arr % 2 == 1, -1, arr)
    print(out)
    print(arr)

def np_stack_demo():
    a = np.arange(10).reshape(2, -1)
    b = np.repeat(1,10).reshape(2, -1)
    c = np.vstack([a,b])
    print(c)
    d = np.hstack([a,b])
    print(d)

def np_create_fix_array():
    arr = np.array([1,2,3])
    a = np.hstack([np.repeat(arr, 3), np.tile(arr, 3)])
    print(a)

if __name__ == '__main__':
    print_version()
    create_array()
    create_array_all_true()
    get_odd_number()
    np_where_demo()
    np_stack_demo()
    np_create_fix_array()