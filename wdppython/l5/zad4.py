def usun_duplikaty(l):#funkcja przyjmuje posortowaną listę
    lista = []
    for i in range(len(l)):
        for j in range(i,len(l)):
            if l[i] == l[j]:
                continue
            lista.append[l[i]]
    return lista

def usun_duplikaty(L):
    if not L:
        return []
    L = sorted(L)
    wynik = [L[0]]
    for i in range(1, len(L)):
        if L[i] != L[i - 1]:
            wynik.append(L[i])
    
    return wynik

def usun_duplikaty(L):
    # Zamiana elementów listy na pary (wartość, pozycja)
    lista_par = [(wartosc, i) for i, wartosc in enumerate(L)]
    
    # Sortowanie listy według wartości
    lista_par.sort(key=lambda x: x[0])
    
    # Przechodzimy przez listę i usuwamy duplikaty wartości
    wynik_pary = []
    ostatnia_wartosc = None
    for wartosc, pozycja in lista_par:
        if wartosc != ostatnia_wartosc:
            wynik_pary.append((wartosc, pozycja))
            ostatnia_wartosc = wartosc
    
    # Sortujemy wynikową listę według pozycji, aby zachować oryginalną kolejność
    wynik_pary.sort(key=lambda x: x[1])
    
    # Tworzymy ostateczną listę wartości bez duplikatów, w oryginalnej kolejności
    wynik = [wartosc for wartosc, _ in wynik_pary]
    return wynik
print(usun_duplikaty([1,2,3,1,2,3,8,2,2,2,9,9,4]))