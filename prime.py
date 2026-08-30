N = int(input("enter an integer"))

factors = 2 

while N >= factors:
    if N % factors==0:
        break
    factors= factors+1

if factors == N:
    print("This is  a prime Number")

else:   
    print("Not a prime Number ")
