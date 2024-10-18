a=[]
s=int(input("enter the size"))
for i in range(s):
    c=int(input("enter the elements"))
    a.append(c)
print(a)
for j in range(s):
    if (a[j]>100):
        a[j]='over'
print(a)
    
    
