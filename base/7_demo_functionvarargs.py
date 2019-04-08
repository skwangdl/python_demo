
def total(a=5, *numbers, **phonebook):
    print('a', a)
    for item in numbers:
        print("numbers:", numbers)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

