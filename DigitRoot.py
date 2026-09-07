N = int(input("Enter the numbers "))

while N >= 10:
    total = 0 
    for digit in str(N):
        total = total + int(digit)
    N = total
print(N)