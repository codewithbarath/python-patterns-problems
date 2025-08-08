def patterns(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(2*i-1):
            if(k%2==0):
                print("A",end="")
            else:
                print("B",end="")
        print()
    for i in range(1,n+1):
        for j in range(i-1):
            print(" ",end="")
        for k in range(2*(n-i)+1):
            if(k%2==0):
                print("A",end="")
            else:
                print("B",end="")
        print()
patterns(5)