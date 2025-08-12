"""
    A
   BC
  DEF
 GHIJ
KLMNO
"""

def numberpattern(n):
    count=65
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(i):
            print(chr(count),end="")
            count+=1
        print()
numberpattern(6)