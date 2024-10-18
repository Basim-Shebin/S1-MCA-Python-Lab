input = str(input("Enter a line of text"))
splitted = input.split(' ')
counted = []
for i in splitted:
    if i not in counted:
        count = splitted.count(i)
        print(f'Count of {i} is {count}')
        counted.append(i)
