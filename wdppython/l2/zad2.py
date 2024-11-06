#idea 1
n = 4
lista = [[" " for i in range(2*n+1)]for i in range(2*n+1)]


for i in range(2*n+1):
    for j in range(2*n+1):
        if i == 2*n or i == 0:
            lista[i][j] = "*"
        if j == 0 or j == 2*n:
            lista[i][j] = "*"
        if j == i:
            lista[i][j] = "*"
            lista[i][-j-1] = "*"
for i in range(len(lista)):
    print(lista[i])
for i in range(len(lista)):
    for j in range(len(lista)):
        print(lista[i][j], end="")
    print()