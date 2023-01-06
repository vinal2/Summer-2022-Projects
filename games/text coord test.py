import random
import time
'''while True:
    random.seed()
    randX = random.randint(0, 10)
    randY = random.randint(0, 10)
    print(randX)
    print(randY)
    print('\n')
    time.sleep(0.5)'''
coord1 = (1, 2)
coord2 = (3, 4)
print(coord1 + coord2)
result = []
x = 0
while x < len(coord1):
    result.append(coord1[x] + coord2[x])
    x += 1
print(result)