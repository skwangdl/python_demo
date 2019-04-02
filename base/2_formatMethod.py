
# format method in python
def demoFormatMethod():
    age = 20
    name = 'hello kepler'
    print('{0}, spring , {1}'.format(age, name))

def demoFormatMethod_double():
    age = 1.0/3
    print('{0:.3f}'.format(age))

def demoFormatMethod_str():
    name = 'hello, my name is kepler'
    print('{0:_^11}'.format(name))

def demoFormatMethod_strWithKey():
    name = '{name} is {my}'
    print(name.format(name='kepler', my='my'))

if __name__ == '__main__':
    demoFormatMethod()
    demoFormatMethod_double()
    demoFormatMethod_str()
    demoFormatMethod_strWithKey()