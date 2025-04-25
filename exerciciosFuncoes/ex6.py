def multiplo(num):
    if num % 7 == 0:
        return num


num = int(input("Digite: "))

for i in range(1,num):
    res = multiplo(i)
    if res is not None:
        print(res)