M = int(input("enter a number"))

factor = 1 
total = 0

for i in range(1 , M//2+1):
    if M % i == 0 :
        total = total + i

if total == M:
    print("This is a perfect number")
else:
    print("This is not a perfect number")

    