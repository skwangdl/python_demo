
# demo about list in python
def demo_list():
    shoplist = ['apple', 'mango', 'carrot', 'banana']
    print('I have ', len(shoplist), 'items to purchase')
    print('These items are: ', end=' ')
    for item in shoplist:
        print(item, end=' ')
    shoplist.append('rice')
    print('My shopping is now: ', shoplist)
    del shoplist[0]
    print('My shopping is now: ', shoplist)
    shoplist.sort()
    print('My shopping is now: ', shoplist)

def demo_tuple():
    zoo = ('python', 'java', 'go')
    print(len(zoo))
    new_zoo = 'ruby', 'csharp', zoo
    print(len(new_zoo))
    print(new_zoo[2][2])


def demo_map():
    map = {'key1': 'value1', 'key2': 'value2'}
    print('key1 value: ', map['key1'])

    for name, address in map.items():
        print('contact {} at {}'.format(name, address))

def demo_sequence():
    list = ['a', 'b', 'c', 'd', 'e']
    print('item 1 to 3 is', list[1:3])

def demo_set():
    bir = set(['a', 'b', 'c', 'd'])
    birc = set(['a', 'b', 'c', 'e'])
    print(birc & bir)
    print(birc | bir)
    print(birc ^ bir)

def demo_str():
    name = 'kepler'
    if name.startswith('k'):
        print('startswith k')
    if 'p' in name:
        print('contain p')
    if name.find('er') != -1:
        print('contain er')
    delimiter = '_*_'
    templist = ['a', 'b', 'c', 'd']
    print(delimiter.join(templist))


if __name__ == '__main__':
    demo_list()
    demo_tuple()
    demo_map()
    demo_sequence()
    demo_set()
    demo_str()