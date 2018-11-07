import math

sum_of_squares = 0
sum_ = 0

for i in range(1, 101):
    sum_of_squares += i**2
    sum_ += i
square_of_sum = sum_**2

print(sum_of_squares)
print(square_of_sum)
input()
difference = square_of_sum - sum_of_squares

print(difference)
input()
    
