"""
    1
   222
  33333
 4444444
"""

def function(n):
    for i in range(1,n+1):
        count=i
        for j in range(n-i):
            print(" ",end="")
        for k in range(2*i-1):
            print(count,end="")
        print()
function(4)