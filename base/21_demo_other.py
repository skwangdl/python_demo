
def get_error_details():
    return (2, 'kepler')

if __name__ == '__main__':
    num, name = get_error_details()
    print('{} {}'.format(num, name))
    name, num = num, name
    print('{} {}'.format(num, name))