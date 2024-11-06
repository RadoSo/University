from duze_cyfry import daj_cyfre

lista = []
liczba = input("podaj liczbe całkowitą: ")#dostajemy w formie str
#wersja switch
for k in range(len(liczba)):
    lista.append(daj_cyfre(int(liczba[k])))
for j in range(5):
    for i in range(len(liczba)):
        print(lista[i][j], end=" ")
    print()