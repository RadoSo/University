def usun_w_nawiasach1(w):#???????????
    arr = []
    s = True
    for i in range(len(w)):
        if w[i] == "(":
            s = False
        elif w[i] == ")":
            s = True
        elif s:
            arr.append(w[i])
        
    print(''.join(arr))


def usun_w_nawiasach(s):
    arr = []
    i = 0
    while i < len(s):
        if s[i] == "(":
            for j in range(len(s[i::])):
                if s[i::][j] == ")":
                    i += j
                    break
        else:
            arr.append(s[i])
        i+= 1
    print("".join(arr))
    

usun_w_nawiasach1("Ala ma kota (perskiego)!")
usun_w_nawiasach1("kot ma(ssssssdddddddddddd) zęby(oooraz)!")
