a=[]
sum1=0
sum2=0
s1=int(input("enter the size"))
for i in range(s1):
    c=int(input("enter the elements"))
    a.append(c)
b=[]
s2=int(input("enter the size"))
for j in range(s2):
    d=int(input("enter the elements"))
    b.append(d)

if (s1==s2):
    print("The lists are of same length")
else:
    print("The lists are not of same size")

for i in range(s1):
    sum1=sum1+a[i]

print("sum of 1st= ",sum1)

for j in range(s2):
    sum2=sum2+b[j]

print("sum of 2nd= ",sum2)

if(sum1==sum2):
    print("the sum are same")
else:
    print("the sum are not same")

common= []
for i in a:
    if i in b:
        common.append(i)

if common:
    print("Common values in both lists:", common)
else:
    print("No common values in both lists")


