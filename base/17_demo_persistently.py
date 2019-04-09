import pickle

def demo_pickle():
    shoplistfile = 'shoplist.data'
    shoplist = ['a', 'b', 'c']
    f = open(shoplistfile, 'wb')
    pickle.dump(shoplist, f)
    f.close()

    del shoplist
    f = open(shoplistfile, 'rb')
    storedlist = pickle.load(f)
    print(storedlist)

if __name__ == '__main__':
    demo_pickle()