S = str(input("Enter a string: "))

S = S.lower()
S = S.replace(" ", "")

reverseS = S[::-1]

if S == reverseS:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")