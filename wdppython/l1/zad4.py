from losowanie_fragmentow import losuj_fragment

def losuj_haslo(n):
    haslo = ""
    while len(haslo) < n:
        frag = losuj_fragment()
        if n - len(haslo) == 1:
            haslo = ""
        elif n - len(haslo) < len(frag):
            pass
        else:
            haslo += losuj_fragment()
    if len(haslo) == n:
        return haslo
    else:
        return losuj_haslo(n)

for i in range(10):
    print(losuj_haslo(8))

for i in range(10):
    print(losuj_haslo(12))
