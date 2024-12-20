
s=input("s:").strip()
if s.isalpha() or " " in s and len(s)>1:
    l=""
    n=len(s)-1
    for i in range(len(s)):   
        if s[n-i]==" ":
            break
        else:
            l=l+s[n-i]
else:
    print(False)
       
l=l[::-1]
print(l,end="")





                 