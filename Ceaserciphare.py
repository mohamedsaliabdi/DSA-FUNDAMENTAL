text = input("Enter text: ")
K = int(input("Enter shift K: "))

encoded = ""

for c in text:
    new_letter = chr((ord(c) - ord('A') + K) % 26 + ord('A'))
    encoded = encoded + new_letter

print("Encoded =", encoded)


decoded = ""

for c in encoded:
    original_letter = chr((ord(c) - ord('A') - K) % 26 + ord('A'))
    decoded = decoded + original_letter

print("Decoded =", decoded)
