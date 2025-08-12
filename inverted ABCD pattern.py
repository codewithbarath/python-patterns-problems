"""
ABCD
EFG
HI
J
"""
def function(n):
    count=65
    for i in range(n,-1,-1):
        for j in range(1,i+1):
            print(chr(count),end="")
            count+=1
        print()
function(4)
