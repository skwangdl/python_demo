import chardet

def demo_chardet():
    print(chardet.detect(b'hello kepler'))
    print(chardet.detect('你愁啥'.encode('gbk')))

if __name__ == '__main__':
    demo_chardet()