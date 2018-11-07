import math
length = 0
index = 2
fib_number = 1
while len(str(fib_number)) < 1000:
    fib_number *= (1 + math.sqrt(5)) / 2
    fib_number = round(fib_number)
    index += 1
print(index)
