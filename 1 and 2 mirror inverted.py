"""
1212
 121
  12
   1
"""
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i-1):
        if(k%2==1):
            print(2,end="")
        else:
            print(1,end="")
    print()
