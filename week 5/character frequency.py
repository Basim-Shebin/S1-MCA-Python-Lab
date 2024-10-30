input_string = "hello world"
char_list = []
for char in input_string:
    found = False
    for item in char_list:
        if item[0] == char:
            item[1] += 1  
            found = True
            break
    if not found:
        char_list.append([char, 1]) 
for item in char_list:
    print(f"'{item[0]}': {item[1]}")
