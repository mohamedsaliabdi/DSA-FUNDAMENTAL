A = int(input("Enter A: "))
B = int(input("Enter B: "))

found = False

for i in range(A, B + 1):

    if i < 2:
        continue

    factors = 2

    while i >= factors:

        if i % factors == 0:
            break

        factors = factors + 1

    if factors == i:
        print(i, end=" ")
        found = True

if found == False:
    print("None")
