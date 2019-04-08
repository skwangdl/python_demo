
# demo about list in python
def method():
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

if __name__ == '__main__':
    method()