M = str(input("Enter a string: "))
N = str(input("Enter a string: "))

if sorted(M) == sorted(N):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
    