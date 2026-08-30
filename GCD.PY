a = int(input("enter a "))
b = int(input("enter b "))

while b!=0:
   reminder = a % b;
   a=b;
   b = reminder;



print(a)