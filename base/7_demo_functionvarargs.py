
def total(a=5, *numbers, **phonebook):
    print('a', a)
    for item in numbers:
        print("numbers:", item)

    for a, b in phonebook.items():
        print(a, b)

if __name__ == '__main__':
    print(total(10,1,2, Jack=123, John=456, Inge=789))
