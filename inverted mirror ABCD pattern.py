"""
ABCD
 EFG
  HI
   J
"""
def function(n):
    count=65
    for i in range(1,n+1):
        for j in range(i-1):
            print(" ",end="")
        for k in range(n-i+1):
            print(chr(count),end="")
            count+=1
        print()

function(4)