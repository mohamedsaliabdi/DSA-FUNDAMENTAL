K = int(input("enter a number a K "))

digits = []

for digit in str(K):
    digits.append(int(digit))

print("digits :" , digits)
print("count :", len(digits))
print("sum :" , sum(digits))