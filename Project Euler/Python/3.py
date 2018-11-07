import math
target = 600851475143
sqrtTarget = round(math.sqrt(600851475143))
total = 1
for x in range(3, sqrtTarget):
    if(target % x == 0):
        print(x)
        total *= x
        if(total == target):
            break
        
