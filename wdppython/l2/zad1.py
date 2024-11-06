#idea 3
n= 4
k =3
counter = 0
def whitlinlenk(k):
    print(" "*k, end="")
def blklinlenk(k):
    print("#"*k, end="")
for i in range(2*n*k):
    counter = i//k
    for j in range(n):
        if counter%2 == 0:
            whitlinlenk(k)
            blklinlenk(k)
        else:
            blklinlenk(k)
            whitlinlenk(k)
    print()
