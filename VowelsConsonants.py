N = input("Enter a string: ")

vowels = "aeiouAEIOU"

vowelcount = 0
consonantscount = 0

for letter in N:

    if letter == " ":
        continue

    if letter in vowels:
        vowelcount += 1
    else:
        consonantscount += 1

print(f"Vowels = {vowelcount}")
print(f"Consonants = {consonantscount}")

