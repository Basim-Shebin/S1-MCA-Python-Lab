string = input("Enter the string: ")
if len(string) < 2:
    new_string = string
else:
    new_string = string[-1] + string[1:-1] + string[0]

print("String with first and last characters exchanged:", new_string)
