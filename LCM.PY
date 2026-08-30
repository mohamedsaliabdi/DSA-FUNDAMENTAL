K = int(input("enter an interger k :"))
S = int(input("enter an integer S "))

orignalK = K;
originalS= S;

while S != 0 :
    reminder = K % S
    K = S;
    S = reminder;

GCD = K
LCM = (orignalK*originalS)//GCD

print(GCD)
print(LCM)
