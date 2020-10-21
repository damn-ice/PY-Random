import math
from time import time

# Speed Decorator ... Tests function speed in milliseconds...
def speed(func):
    def wrapper(*args, **kwargs):
        t1 = time()*1000
        func(*args, **kwargs)
        t2 = time()*1000
        return print(t2-t1)
    return wrapper

def conversionArray(item):
    binaryList = []
    while item > 0:
        # We can simpy use floor division i.e 3//2 = 1
        deci, integ = math.modf(item / 2)
        item = integ
        if deci > 0:
            binaryList.append(1)
        else:
            binaryList.append(0)
    if len(binaryList) < 8:
        numb = 8 - len(binaryList)
        for _ in range(numb):
            binaryList.append(0)

    if len(binaryList) > 8:
        to_add = len(binaryList) % 4
        if to_add:
            to_add = 4 - to_add
            for _ in range(to_add):
                binaryList.append(0)
    return binaryList


def decTobinary(number):
    array = conversionArray(number)
    answer = "".join(map(str, array))
    return answer[::-1]

# print(decTobinary(25699993))




decTobinary(25699993)

