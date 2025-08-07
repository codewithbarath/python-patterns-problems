def invertedpattern(n):
    for i in range(1,n+1):
        for j in range(i-1):
            print(" ",end="")
        for k in range(1,2*(n-i)):
            print(k,end="")
        print()
invertedpattern(5)