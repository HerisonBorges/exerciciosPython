def calc(num):
    if num % 2 == 0:
        return num
    return None


for i in range(1001):
    res = calc(i)
    if res is not None:
        print(res)