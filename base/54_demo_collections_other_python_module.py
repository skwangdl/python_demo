from collections import namedtuple, deque, defaultdict, OrderedDict, Counter
import base64
import struct
import hashlib
import hmac
import itertools

def demo_namedtuple():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1,2)
    print(p.x)
    print(p.y)

def demo_deque():
    q = deque(['a','b','c'])
    q.append('x')
    q.appendleft('y')
    print(q)

def demo_defaultdict():
    dd = defaultdict(lambda :'N/A')
    print(dd['key'])

def demo_orderedDict():
    od = OrderedDict([('a', 1), ('b', 3), ('c', 2)])
    print(od)

def demo_counter():
    c = Counter()
    for x in 'aaabbvvcc':
        c[x] = c[x] + 1
    print(c)

def demo_base64():
    t = base64.b64encode(b'kepler')
    print(t)

def demo_struct():
    a = struct.pack('>I', 10240099)
    print(a)

def demo_hashlib():
    md5 = hashlib.md5()
    md5.update('hello kepler'.encode('utf-8'))
    print(md5.hexdigest())
    md5.update('hello kepler1'.encode('utf-8'))
    print(md5.hexdigest())

def demo_hmac():
    t = hmac.new('kepler'.encode('utf-8'), 'key'.encode('utf-8'), 'MD5').hexdigest()
    print(t)

def demo_itertools():
    nature = itertools.count(1)
    ns = itertools.takewhile(lambda x: x <=10, nature)
    print(list(ns))

    for key, group in itertools.groupby('AAaBBbCCCc', lambda x:x.upper()):
        print(key, list(group))

if __name__ == '__main__':
    demo_namedtuple()
    demo_deque()
    demo_defaultdict()
    demo_orderedDict()
    demo_counter()
    demo_base64()
    demo_struct()
    demo_hashlib()
    demo_hmac()
    demo_itertools()