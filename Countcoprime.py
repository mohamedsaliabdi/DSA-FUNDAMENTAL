
N = int(input("Enter N: "))

count = 0

for i in range(1, N + 1):

    a = i
    b = N

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    if a == 1:
        count = count + 1

print(count)
