import re

def demo_re():
    re_telephone = re.compile(r'^(\d{3})-(\d{3,8})/div>')
    match = re.match(r'^\d{3}\-\d{3,8}/div>', '010-12345')
    print(match)
    a = re.split(r'[\s\,\;]+', 'a,b;;  c  d')
    print(a)
    temp = re_telephone.match('010-8089').groups()
    print(temp)

def demo_re_greed():
    r = re.match(r'^(\d+)(0*)/div>', '102300').groups()
    print(r.__str__())

def demo_re_ungreed():
    r = re.match(r'^(\d+?)(0*)/div>', '102300').groups()
    print(r.__str__())

if __name__ == '__main__':
    demo_re()
    # demo_re_greed()
    # demo_re_ungreed()