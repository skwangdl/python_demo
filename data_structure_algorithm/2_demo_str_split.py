
# 如果一个可迭代对象的元素个数超过变量个数时会抛出一个ValueError。那么怎样才能从这个可迭代对象中解压出N个元素出来
def demo_str_split():
    line = 'a:c,d,e,f,g:faf'
    str1, *str2, str3 = line.split(':')
    print(str2)
    record = ('ACME', 50, 123,4, (12, 18,2012))
    name, *_, (*_, year) = record
    print('{} {}'.format(name, year))

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

if __name__ == '__main__':
    demo_str_split()
    items = [1,10,4,7,2,3]
    print(sum(items))