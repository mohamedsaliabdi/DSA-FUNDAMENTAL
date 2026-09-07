N = int(input("Enter a number "))

for rows in range (1 , N+1):


    for j in range(N-rows):
        print(" " , end="")

    for j in range (2*rows-1):
        print("*" , end="")
    print()

# # Outer loop = rows
# First inner loop = print spaces (N - i)
# Second inner loop = print stars (2*i - 1)
# Spaces go down, stars go up