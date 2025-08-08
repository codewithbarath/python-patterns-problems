def function(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(1,i+1):
            if(k%2==0):
                print("B",end="")
            else:
                print("A",end="")
        print()
function(5)