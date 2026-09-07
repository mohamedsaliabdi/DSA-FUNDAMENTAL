A = int(input("Enter the first number: "))
B = int(input("Enter the second Number "))

total = 0 
for i in range (A , B+1):
    if i % 2 == 1:
        total = total+i
print(total)