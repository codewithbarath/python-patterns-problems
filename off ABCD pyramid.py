"""
        A
      B C D
    E F G H I
  J K L M N O P
G R S T U V W X Y
"""

def patterns(n):
    count=65
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(2*i-1):
            print(chr(count),end="")
            count+=1
        print()
patterns(5)
