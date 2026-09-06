sideA = int(input("Enter the length of side A: "))
sideB = int(input("Enter the length of side B: "))
sideC = int(input("Enter the length of side C: "))

if sideA + sideB > sideC and sideA + sideC > sideB and sideB + sideC > sideA:
    print("The triangle is valid.")
    if sideA == sideB == sideC:
        print("The triangle is equilateral.")
    elif sideA == sideB or sideA == sideC or sideB == sideC:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("The triangle is not valid.")