N = int(input("Enter a number: "))

digit_sum = 0

for digit in str(N):
    digit_sum = digit_sum + int(digit)

if N % digit_sum == 0:
    print("Harshad")
else:
    print("Not Harshad")