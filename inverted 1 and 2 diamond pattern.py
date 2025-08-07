n=7
for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(2*(n-i)+1):
        if(k%2==1):
            print(2,end="")
        else:
            print(1,end="")
    print()