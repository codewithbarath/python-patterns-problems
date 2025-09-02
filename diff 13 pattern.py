def function(n):
    for i in range(n):
        for j in range(n):
            if(i%2!=0 and j==0):
                print(" ",end="")
            elif(i%2==0 and j==n-1):
                print(" ",end="")
            else:
                print("*",end="")
        print()
function(5)