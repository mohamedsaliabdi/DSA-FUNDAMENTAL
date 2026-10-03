N = int(input("enter an integer"))

factors = []

while N % 2 == 0:
    factors.append(2)
    N = N // 2


P = 3
while P * P <= N:
    while N % P == 0:
        factors.append(P)
        N = N // P
    P += 2

if N > 1:
    factors.append(N)

print("Prime factors:", factors)