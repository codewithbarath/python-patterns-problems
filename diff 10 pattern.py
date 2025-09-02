def function(n):
    for i in range(n):
        row=[]
        for j in range(n+3):
            if(i==0 and (i==j or i+j==n+3-1)):
                print("*",end="")
            elif(i==0+1 or (i==j or i+j==n+3-2)):
                print("*",end="")
            else:
                print("n",end="")
        print()
function(4)