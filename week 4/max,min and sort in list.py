a=[]
b=int(input("enter the size "))
for i in range(b):
    c=int(input("enter the values "))
    a.append(c)

print("The given list is ",a)
max=max(a)
min=min(a)
asc=sorted(a)
print("max value of list is",max)
print("min value of list is",min)
print("Sorted list is ",asc)
asc.reverse()
print("reverse sorted list is ",asc)
