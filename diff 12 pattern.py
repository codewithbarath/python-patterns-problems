def function(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or j==0 or i==n-1 or j==n-1):
                print("E",end="")
            elif(i+j==n-1 and i==j):
                print("C",end="")
            else:
                print("D",end="")
          
        print()
function(5)