# demo method use default parameter
def say(message, time = 1):
    print(message)
    print(time)

if __name__ == '__main__':
    say('hello')
    say('hello', 2)