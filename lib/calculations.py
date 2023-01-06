import math
import sys

sys.path.insert(0, '/Users/CREEP/Downloads/python/lib')

alphabetList = [chr(i) for i in range(ord('a'),ord('z')+1)]
output = ''

def findMod(num, mod):
    modRem = num % mod
    num = (num - modRem) / mod
    return num

def convertDecimal(num):
    global alphabetList
    global output
    if num > 0:
        dogZeros = int(math.log10(num))
        if dogZeros >= 3:
            if dogZeros % 3 == 0:
                currentDigit = dogZeros
            else:
                currentDigit = findMod(dogZeros, 3) * 3
            dogReduced = num / pow(10, currentDigit)
            output = str(round(dogReduced, 2)) + alphabetList[int(findMod(dogZeros, 3) - 1)]
        else:
            return str(round(num, 2))
    else:
        return str(round(num, 2))
    return str(output)
    

def addCoord(self, other):
    x = 0
    result = []
    while x < len(self):
        result.append(self[x] + other[x])
        x += 1
    return result
