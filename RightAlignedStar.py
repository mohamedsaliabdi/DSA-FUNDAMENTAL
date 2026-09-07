N = int(input("Enter a number "))

for i in range(1 , N+1):
    for star in range(i):
        print("*", end="")
    print()