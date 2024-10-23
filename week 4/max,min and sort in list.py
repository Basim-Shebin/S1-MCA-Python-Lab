a=[]
b=int(input("enter the size "))
for i in range(b):
    c=int(input("enter the values "))
    a.append(c)
print("The given list is ",a)
max=max(a)
min=min(a)
print("max value of list is",max)
print("min value of list is",min)
a.sort()
print("The sorted list is ",a)
a.reverse()
print("The reverse of the list is ",a)

