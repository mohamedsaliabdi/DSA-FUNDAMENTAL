K = int(input("enter a an integer K"))

digits = [];

for digit in str(K):
    digits.append(int(digit))



originaldigits = digits.copy()
print(originaldigits)

digits.reverse()

rever = 0 

for digit in digits:
    rever = rever * 10 + digit

print(rever)

originalrever = 0
for digit in originaldigits:
    originalrever = originalrever*10+digit

print(originalrever)


if rever == originalrever:
    print("This palindrome")
else:
    print("This is not palindrome")