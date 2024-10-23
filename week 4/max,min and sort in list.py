a = []
b = int(input("Enter the size: "))
for i in range(b):
    c = int(input("Enter the values: "))
    a.append(c)

print("The given list is:", a)

max_value = max(a)
min_value = min(a)
count = len(a)
total_sum = sum(a)
print("Max value of list is:", max_value)
print("Min value of list is:", min_value)
print("Count of elements in the list is:", count)
print("Sum of elements in the list is:", total_sum)
a.sort()
print("The sorted list is:", a)
a.reverse()
print("The reverse of the list is:", a)
