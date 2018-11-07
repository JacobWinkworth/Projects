counter_list = [1]
num_list = []
for x in range(2, 999999):
    counter = 0
    num = x
    while(x > 1):
        if(x % 2 == 0):
            x = x / 2
        else:
            x = (3 * x + 1)
        counter += 1
    if(counter > max(counter_list)):
        counter_list.append(counter)
        num_list.append(num)
print("cunt")
print(num_list[len(num_list) - 1])
