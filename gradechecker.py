Grade = int(input("Enter your grade: "))

if Grade >= 90:
    print("Your grade is A")

elif Grade >= 75 and Grade <= 89:
    print("Your grade is B")

elif Grade >= 60 and Grade <= 74:
    print("Your grade is C")

elif Grade >= 50 and Grade <= 59:
    print("Your grade is D")

elif Grade < 50:
    print("Your grade is F")