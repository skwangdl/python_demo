import pickle

def demo_pickle():
    d = dict(name='kepler', age='27')
    p = pickle.dumps(d)
    with open('../temp/pickle.txt', 'wb') as file:
        file.write(p)
    with open('../temp/pickle.txt', 'rb') as file:
        obj = pickle.load(file)
        print(obj)

if __name__ == '__main__':
    demo_pickle()