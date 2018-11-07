import math
num = 1
total = 0
goldenRatio = float((1 + math.sqrt(5)) / 2)
while(num <= 4000000):
    if (num % 2 == 0):
        total += num
        print(num)
    num = round(num * goldenRatio)
print(total)
    
    
