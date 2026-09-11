A = [1, 2, 3]
B = [4, 5, 6]

i = 0
j = 0 

merhged = []
while i < len(A) and j < len(B):
    if A[i] < B[j]:
        merhged.append(A[i])
        i += 1
    else:
        merhged.append(B[j])
        j += 1
while i < len(A):
    merhged.append(A[i])
    i += 1
while j < len(B):
    merhged.append(B[j])
    j += 1
print(merhged)