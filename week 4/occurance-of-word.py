string =input("Enter a line of text: ")
w=input("enter the word ")
a=[]
count=0
a=string.split(" ")
for i in range(0,len(a)):
    if(w==a[i]):
        count=count+1
print("count of word is : ",count)
