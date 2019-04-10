from functools import reduce

def lambda_list_1():
    return list(filter(lambda x : True if x % 3 == 0 else False, range(100)))

def lambda_list_2():
    return list(filter(lambda x: x % 3 == 0, [1,2,3]))

def lambda_map():
    return list(map(lambda x:x + 1, [1,2,3]))

def lambda_sort():
    return list(sorted([2,1,3], key=lambda x:x))

def lambda_reduce():
    return reduce(lambda a, b:'{} {}'.format(a,b), [1,2,3])

if __name__ == '__main__':
    print(lambda_list_1())
    print(lambda_list_2())
    print(lambda_map())
    print(lambda_sort())
    print(lambda_reduce())