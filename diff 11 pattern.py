n=3
count=1
for i in range(n):
    arr=[]
    for j in range(n):
        arr.append(count)
        count+=1
    
    if i==1:
        for j in range(n-1,-1,-1):
            print(arr[j],end=" ")
    else:
        for j in range(n):
            print(arr[j],end=" ")
    print()