# Print a numerical triangle of height n without using strings.
# Each line i contains the digit i repeated i times, using only arithmetic operations.

for i in range(1, int(input())):
    print(i * (10**i - 1) // 9)
