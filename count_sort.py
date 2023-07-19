arr=list(map(int,input("Enter the array elements: ")))
max_num= max(arr)
min_num = min(arr)
diff = max_num-min_num
l =[0]*(max_num+1)
for i in arr:
    l[i]+=1
lst=[]
for j in range(len(l)):
    if l[j]>0:
        for i in range(l[j]):
            lst.append(j)
print(lst)

