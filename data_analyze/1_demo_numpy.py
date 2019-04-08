import numpy as np
from numpy import pi

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

def method_arange():
    g = np.arange(10,30,5)
    print(g)

def method_linspace():
    h = np.linspace(10,20,9)
    print(h)

def method_calculator():
    a = np.ones((2,3), dtype=int)
    b = np.random.random((2,3))
    a *= 3
    print(a)
    b += a
    print(b)

def method_transform():
    a = np.ones(3, dtype=np.int32)

if __name__ == '__main__':
    method()
    method_createArray()
    method_num()
    method_createOnesArray()
    method_createZeroArray()
    method_empty()
    method_arange()
    method_linspace()
    method_calculator()