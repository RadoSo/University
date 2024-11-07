def F(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

# corrected function f, adjusted for reccurency and counter
def energia(n,licznik=0):
    if n == 1:
        return licznik
    if n % 2 == 0:
        return energia(n / 2,licznik+1)
    else:
        return energia(3 * n + 1, licznik+1)
print(energia(7))#energia liczby 7 powinna byc == 16 z przykladu
def energyrange(a,b):
    energylist = [energia(n) for n in range(a,b+1)]
    #srednia
    sum = 0
    for i in energylist:
        sum += i
    print(f"srednia = {sum/(b+1-a)}")
    #mediana
    if (b+1-a)%2 == 0:
        print(f'mediana = {(energylist[b-a-1]+energylist[b-a])/2}')
    else:
        print(f'mediana = {energylist[b-a]}')
    #max
    print(f"max = {max(energylist)}")
    #min
    print(f"min = {min(energylist)}")

    return energylist
energyrange(7,7)#baseline test
