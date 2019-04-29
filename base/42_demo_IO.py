
def demo_io():
    # a:append  r:read  w:write
    with open('../temp/test.txt', 'a') as f:
        f.write('hello SK1\n')

if __name__ == '__main__':
    demo_io()