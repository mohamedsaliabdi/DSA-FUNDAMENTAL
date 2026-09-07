N = int(input("Enter a number "))

for rows in range(N , 0 , -1):
    for star in range(rows):
        print("*", end="")
    print()