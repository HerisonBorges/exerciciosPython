def mult(num):
    if num % 10 == 0:
        return num
    return None

for i in range(101):
    res = mult(i)
    if res is not None:
        print(res, "Multiplo de 10")