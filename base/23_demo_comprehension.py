
def tempmethod():
    listone = [2,3,4]
    listtwo = [2*i for i in listone if i > 2]
    print(listtwo)

def powersum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    print(total)

if __name__ == '__main__':
    tempmethod()
    powersum(2,3,4)# 3^2 + 4^2