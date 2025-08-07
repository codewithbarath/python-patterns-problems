"""
    1
   12
  121
 1212
"""
n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        if(k%2==1):
            print(1,end="")
        else:
            print(2,end="")
    print()