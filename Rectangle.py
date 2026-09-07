M = int(input("Enter the row"))
N = int(input("Enter the columns"))

for rows in range (M):
    for j in range(N):
        if rows == 0 or rows == M-1 or j == 0 or j == N-1:
            print("*" , end="")
        else:
            print(" " , end="")
    print()