import sys
import time

def temp():
    f = None
    try:
       with open("D:\\temp\\pome.txt") as f:
           for line in f:
               print(line, end=' ')
    except IOError:
        print("could not find file pome.txt")
    except KeyboardInterrupt:
        print("!! you cancelled the reading from the file")
    finally:
        if f:
            f.close()
        print("(cleaning up: Closed the file)")

if __name__ == '__main__':
    temp()