arr = [1, 2, 2, 3, 3, 3,4]

counts = {}
for n in arr:
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1
print(counts)