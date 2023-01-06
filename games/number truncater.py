from functionFile import *
import sys

sys.path.insert(0, '/Users/CREEP/Downloads/python/lib')

import math
import time
from calculations import *

dog = 1000000
dogReduced = 0
currentDigit = 0
alphabetList = [chr(i) for i in range(ord('a'),ord('z')+1)]

while True:
    dogZeros = int(math.log10(dog))
    if dogZeros >= 3:
        if dogZeros % 3 == 0:
            currentDigit = dogZeros
        else:
            currentDigit = findMod.findMod(dogZeros, 3) * 3
        dogReduced = dog / pow(10, currentDigit)
        output = str(round(dogReduced, 2)) + alphabetList[int(findMod.findMod(dogZeros, 3) - 1)]
    print(output),
    time.sleep(0.1)
