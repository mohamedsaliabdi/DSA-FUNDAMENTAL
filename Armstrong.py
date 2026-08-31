N = int(input("enter a integer N "))

digits = []
count = 0
sum = 0

for digit in str(N):
    digits.append(int(digit))
    count=count+1;


for digit in digits:
    digit = digit ** count
    sum = sum + digit

if sum == N :
    print("Armstrong")
else:
    print("Not Armstrong")


