date = int(input("Enter a year: "))
leap_years =[]

for y in range(2024, date + 1):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        leap_years.append(y)

print(leap_years)
