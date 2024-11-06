n = int(input("Enter the number of elements in the list: "))
numbers = []

for i in range(0,n):
    num = int(input("Enter The number "))
    numbers.append(num)

while True:
    print("\n****MENU****\n")
    print("1. GREATEST and LOWEST")
    print("2. SORT")
    print("3. LIST OF EVEN NUMBERS")
    print("4. EXIT")
    
    choice = input("Enter your choice ")

    if choice == '1':
        greatest = max(numbers)
        lowest = min(numbers)
        print("The greatest number is: ",greatest)
        print("The lowest number is: ",lowest)

    elif choice == '2':
        sorted_num = sorted(numbers)
        print("The sorted list is:",sorted_num)

    elif choice == '3':
        even=[]
        for num in numbers:
            if num %2==0:
                even.append(num)
        print("The sorted list is : ",even)
        
    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("WRONG CHOICE ! enter a choice between 1-4.")
