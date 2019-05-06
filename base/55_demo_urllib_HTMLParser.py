from urllib import request
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)
    def handle_endtag(self, tag):
        print('</%s>' % tag)
    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)
    def handle_data(self, data):
        print(data)
    def handle_comment(self, data):
        print('<!--', data, '-->')
    def handle_entityref(self, name):
        print('&%s;' % name)
    def handle_charref(self, name):
        print('&#%s;' % name)

def demo_urllib():
    with request.urlopen('https://www.baidu.com') as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k,v))
        print('Data: ', data.decode('utf-8'))
        return data.decode('utf-8')

if __name__ == '__main__':
    data = demo_urllib()
    parser = MyHTMLParser()
    parser.feed(data)