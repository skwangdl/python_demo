
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

def demo_openfile():
    poem = '''\
    hello
    kepler
    '''
    f = open('D:\\temp\\pome.txt', 'w')
    f.write(poem)
    f.close()
    f = open('D:\\temp\\pome.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end=' ')
    f.close()

if __name__ == '__main__':
    msg = "abccba"
    print(is_palindrome(msg))
    demo_openfile()