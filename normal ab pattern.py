n=5
for i in range(1,n+1):
    for j in range(i):
        if(j%2==0):
            print("A",end="")
        else:
            print("B",end="")
    print()