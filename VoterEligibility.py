Age = int(input("Enter your age: "))

citizenship = int(input("Enter citizenship 1 or 0: "))

disqualification = int(input("Enter disqualification 1 or 0: "))


if Age < 18:
    print("Not Eligible - Too young")

elif citizenship == 0:
    print("Not Eligible - Not a citizen")

elif disqualification == 1:
    print("Not Eligible - Disqualified")

else:
    print("Eligible")