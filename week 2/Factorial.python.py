a=int(input("enter the number "))
fact=1
if a<0:
    print("no factorial")
elif a==0:
    print("the factorial of 0 is 0")
else:
    for i in range(1,a+1):

        fact*=i
        print("The Factorial of ",a," numbers is ",fact)
