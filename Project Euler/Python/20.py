factorial = 1
sum_of_factorial = 0
for x in range(1, 100):
    factorial *= x
for char in str(factorial):
    sum_of_factorial += int(char)
print(sum_of_factorial)
