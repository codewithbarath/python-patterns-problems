
n=5
for i in range(1,n):
    for j in range(n-i):
        print(" ",end="")
    z=2*i-1
    if (i>1):
        m=(z//2)
    else:
        m=1
    for k in range(1,z+1):
        if(k<=m):
            print(k,end="")
        else:
            count=2
            print(k-count,end="")
            count-=2
    print()
    
