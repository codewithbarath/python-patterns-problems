"""
QRSTUVWXY
 JKLMNOP
  EFGHI
   BCD
    A
"""
def function(n):
    
    for i in range(1,n+1):
        if(i==1):
            count=81
        elif(i==2):
            count=74
        elif(i==3):
            count=69
        elif(i==4):
            count=66
        else:
            count=65
        for j in range(i-1):
            print(" ",end="")
        for k in range(1,2*(n-i)):
            if(i==1):
                print(chr(count),end="")
                count+=1
            elif(i==2):
                print(chr(count),end="")
                count+=1
            elif(i==3):
                print(chr(count),end="")
                count+=1
            elif(i==4):
                print(chr(count),end="")
                count+=1
            else:
                print(chr(count),end="")
        print()

function(6)