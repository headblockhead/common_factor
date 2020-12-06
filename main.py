num1 = input("Number 1:")
num2 = input("Number 2:")
factorsnum1 = list(range(0))
factorsnum2 = list(range(0))
for i in range(1, int(num1) + 1):
    if int(num1) % i == 0:
        factorsnum1.append(i)
print(factorsnum1)
for i in range(1, int(num2) + 1):
    if int(num2) % i == 0:
        factorsnum2.append(i)
print(factorsnum2)
for i in factorsnum1:
    for j in factorsnum2:
        if i == j:
            print(j)