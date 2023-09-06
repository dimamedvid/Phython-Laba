while True:
    a = float(input("Введіть число а:"))
    b = float(input("Введіть число b:"))
    if a > 0 and b > 0:
        break
    else:
        print("Ви ввели від'ємне число, введіть заново числа")
X = 0
if a > b:
    X = (a*b-1)
elif  a == b:
    X = (225)
if a < b:
    X = ((a-5)/b)
print(X)
