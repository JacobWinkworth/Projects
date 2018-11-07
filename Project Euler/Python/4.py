length = 0
for x in range(100, 999):
    for i in range(100, 999):
        measure = 0
        product = x * i
        product = str(product)
        reverse_product = product[::-1]
        length = len(product) - 1
        for k in range(0, length):
            if product[k] != reverse_product[k]:
                break
            measure += 1
            if measure == length:
                print(product)
