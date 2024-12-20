digits=[4,5,6,9]
if digits[-1]==9:
    digits.pop(-1)
    digits.append(1)
    digits.append(0)  
else:
    l=int(digits[-1])+1
    digits.append(l)   
    digits.pop(-2)     

print(digits)