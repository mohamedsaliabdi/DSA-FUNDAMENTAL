N = int(input("Enter number of rows: "))

number = 1

for i in range(1, N + 1):

    for j in range(i):
        print(number, end=" ")
        number = number + 1

    print()
