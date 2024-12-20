num=[-1,0,1,2,-1,-4]
l={}
s=set()
for i, nums in enumerate(num):
    l[nums]=i
for i in range(len(num)):
    for j in range(i+1,len(num)):
        target=-num[i]-num[j]
        if target in l and l[target]!=i and l[target]!=j:
            s.add(tuple(sorted([num[i],num[j],target])))
            


L=list(s)
print(L)