def circle(n,przesuniecie = 0):
    r = n/2
    for y in range(n):
        print(przesuniecie*" ",end="")
        for x in range(n):
            if (x-r+ 0.5)**2 + (y-r + 0.5)**2 <= r**2: 
                print("*", end="")
            else:
                print(" ",end="")
        print()
circle(27,12)
circle(37,7)
circle(47,2)