import math
def erastotenesa(n):
    lp = [i for i in range(2,n+1)]
    count = 0
    for _ in range(int(n**0.5)-1):
        if lp[count] != 0:    
            k = lp[count]
            
            for l in range(k**2-2,n-1,k):
                lp[l] = 0
        count += 1
    return lp
# print(erastotenesa(30))

def palindromy(a,b):
    b = b+2
    lp = [0,0]+erastotenesa(b)
    for i in range(a,b-1):
        if str(lp[i]) == str(lp[i])[::-1] and lp[i]!= 0:
            print(lp[i])
palindromy(10,1000000)