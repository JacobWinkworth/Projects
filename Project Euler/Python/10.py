import math
for x in range(1, 2000000):
    root_x = math.sqrt(x)
    for i in range(1, root_x):
        if(x % i == 0):
            break
        
        
