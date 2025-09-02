
"""
43334
43334
43334
44444
"""
def function(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or j== 0 or i==n-1 or j==n-1):
                print("4",end="")
            else:
                print("3",end="")
        print()
function(5)