def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return(prime)
liczba = 12823777

def sevens(liczba, rq):
    count = 0
    for i in str(liczba):
        count+=1
        if i != "7":
            count = 0
        if count >= rq:
             return True
    return False

count= 0
primes = SieveOfEratosthenes(100_000)
for i in range(len(primes)):
    if primes[i] and sevens(i,3):
        count+=1
        print(i,count)
