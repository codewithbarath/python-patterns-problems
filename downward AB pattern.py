def function(n):
    for i in range(n,-1,-1):
        for j in range(1,i+1):
            if(j%2==0):
                print("B",end="")
            else:
                print("A",end="")
        print()
function(6)
