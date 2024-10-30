start = 1000
end = 9999

a = []
for i in range(int(start**0.5), int(end**0.5) + 1):
    square = i * i
    if square >= start and square <= end:
        all_even = True
        for digit in str(square):
            if int(digit) % 2 != 0:
                all_even = False
                break
        if all_even:
            a.append(square)

print("Four-digit perfect squares with all even digits:")
print(a)
