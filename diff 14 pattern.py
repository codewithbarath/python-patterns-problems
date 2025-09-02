def function(n):
    count=1
    for i in range(n):
        for j in range(n):
            if(i==0 and (i==n-1 or j!=n-1)):
                print(count,end="")
                count+=1
        print()
function(5)