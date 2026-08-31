K = int(input("enter a number  K :"))

digits = [];

for digit in str(K):
    digits.append(int(digit))

digits.reverse()

rever = 0
for digit in digits:
    rever = rever * 10 + digit

print(rever)
