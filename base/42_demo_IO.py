from io import StringIO
from io import BytesIO
import os

def demo_io_file():
    # a:append  r:read  w:write
    with open('../temp/test.txt', 'a') as f:
        f.write('hello SK1\n')

def demo_io_StringIO():
    f = StringIO()
    f.write('hello')
    f.write(' ')
    print(f.getvalue())
    x = StringIO('kepler\nhello\nworld')
    while True:
        s = x.readline()
        if s == '':
            break
        print(s.strip())

def demo_io_BytesIO():
    f = BytesIO()
    f.write('您好'.encode('utf-8'))
    print(f.getvalue())

def demo_io_os():
    print(os.name)
    print(os.environ)
    print(os.environ.get('MAIL_PWD'))
    print(os.path.abspath('.'))
    testpath = os.path.join(os.path.abspath('.'), 'test')
    os.mkdir(testpath)
    os.rmdir(testpath)
    print(os.path.split(testpath))
    print(os.path.splitext('../temp/test.txt'))

def demo_io_filter_file():
    print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])



if __name__ == '__main__':
    # demo_io_file()
    # demo_io_StringIO()
    # demo_io_BytesIO()
    # demo_io_os()
    demo_io_filter_file()