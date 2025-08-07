"""
1 2 3 4
  1 2 3
    1 2
      1
   
"""
def pattern(n):
    for i in range(1,n+1):
        for j in range(i-1):
            print(" ",end="")
        for k in range(1,n-i+1):
            print(k,end="")
        print()
pattern(5)