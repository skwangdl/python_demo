import numpy as np

def method():
    a = np.arange(15).reshape(3,5)
    print(a)
    print(a.shape)
    print(a.ndim)
    print(a.dtype.name)
    print(a.itemsize)

def method_createArray():
    b = np.array([1,2,3,4])
    print(type(b))
    print(b.dtype)

def method_num():
    c = np.array([[1,2], [3,4]], dtype=complex)
    print(c)

def method_createZeroArray():
    d = np.zeros((3,4))
    print(d)

def method_createOnesArray():
    e = np.ones((3,4))
    print(e)

def method_empty():
    f = np.empty((2,3))
    print(f)

if __name__ == '__main__':
    method()
    method_createArray()
    method_num()
    method_createOnesArray()
    method_createZeroArray()
    method_empty()