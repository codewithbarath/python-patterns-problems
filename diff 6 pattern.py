"""
  *  
 * * 
*   *
 * * 
  * 
"""
def function(n):
    if(n%2!=0):
        m=(n-1)//2
        print(m)
        for i in range(n):
            for j in range(n):
                if(i+j==m or i+j==m+(n-1) or (i+j==m+(n//2) and i!=0 and j!=0 and i!=j)):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
function(5)
