##write a python program to calculate total marks and percentage of 5 subjects##
##write a pyhon program  to swapthe values without using temperory variables##
##write a program tom input a number then increment the number by 5 and decrement the number by 3##

print("Enter the marks out of 20")
a=int(input("Enter the marks 1 "))
b=int(input("Enter the marks 2 "))
c=int(input("Enter the marks 3 "))
d=int(input("Enter the marks 4 "))
e=int(input("Enter the marks 5 "))

s=a+b+c+d+e
Per=(s/100)*100
print("Total Marks Obtained = ",s)
print("Percentage = ",Per,"%")
