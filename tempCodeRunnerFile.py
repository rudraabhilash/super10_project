
#import re

'''text = "My phone 838281jkl4845 number is 123-456-7890."
numbers = re.findall(r"\d+", text)
print(numbers)  # Output: ['123', '456', '7890']

text = "Hello, world!"
if re.match(r"Hello", text):
    print("Match found!")

text = "I love cats!"
new_text = re.sub(r"cats", "dogs", text)
print(new_te'''

'''for i in range(4):
    for j in range(i+1,6):
        for k in range(6):
            if i==k or j==k or i==k:
                continue
            else:
                print([i,j,k])'''

'''l=[45,1,122,415,1,2,1]
s=set()
s.add(tuple(l))
print(s)'''

'''nums=[-1,0,1,2,-1,-4]
s=set()
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==0:
                s.add(tuple(sorted([nums[i],nums[j],nums[k]])))

'''L=list(s)
print(L)
list1=[3,5,2,9,5]
list2=[1,6,9,5,3,4,10,2,]'''
s=set()
l1=sorted(list1)
l2=sorted(list2)
for i in l1:
    for j in l2:
        if i>=j:
            s.add(j)
            s.add(i)
        else:
            s.add(i)
            s.add(j)
print(s)'''
            
        