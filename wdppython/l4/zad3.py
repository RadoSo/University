"""Napisz funkcję randperm(n) która losuje permutację liczb od 0 do n - 1 (czyli ma
zwracać wylosowaną listę o długości n zawierającą wszystkie liczby z zadanego przedziału). Przygotuj
prezentację tej funkcji, która wypisuje kilka losowych permutacji dla liczb z przedziału od 0 do 9. Nie
wolno korzystać z funkcji shuffle ani z funkcji sample z modułu random (ale sprawdź, co one robią).
Za to zadanie można dostać premię 0.5p (nie wliczającą się do maksimum), jeżeli funkcja randperm
będzie poprawna, będzie losować każdą permutację z tym samym prawdopodobieństwem, a ponadto x
= randperm(10 ** 6) wykona się w kilka sekund"""
import random
def randperm(n):
    perm = list(range(n))
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        perm[i], perm[j] = perm[j], perm[i]
    
    return perm

print(randperm(10**7))
