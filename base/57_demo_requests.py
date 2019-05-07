import requests

def demo_requests():
    r = requests.get('https://www.baidu.com')
    print(r.headers)
    print(r.content)

if __name__ == '__main__':
    demo_requests()