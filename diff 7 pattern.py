def function(n):
    count=1
    for i in range(1,n+1):
        row=[]
        for j in range(1,n+1):
            row.append(count)
            count+=1
        if i%2==0:
            for k in range(len(row)-1,-1,-1):
                print(row[k],end=" ")
        else:
            for k in range(len(row)):
                print(row[k],end=" ")
        print()
function(4)
