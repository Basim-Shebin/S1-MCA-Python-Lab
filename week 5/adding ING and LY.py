input_string = input("Enter a string: ")
length = len(input_string)
if length >= 3 and input_string[length - 3:length] == "ing":
    result_string = input_string[:-3] + "ly"
else:
    result_string = input_string + "ing"
print("Result:", result_string)
