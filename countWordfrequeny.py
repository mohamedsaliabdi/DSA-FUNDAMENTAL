S = str(input("Enter a string: "))
W = str(input("Enter a word to count its frequency: "))


S = S.lower()
W = W.lower().strip()

S = S.split()
count = 0 

for word in S:
    if word == W:
        count += 1

print(f"The word '{W}' appears {count} times in the string.")