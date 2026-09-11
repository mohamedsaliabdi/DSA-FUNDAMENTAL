Numbers = input("Enter numbers separated by spaces: ")

arr = Numbers.split()

print(arr)
sum = 0
for n in arr:
    sum += int(n)
print("Sum =", sum)
print("Average =", sum / len(arr))
numbers = []
for n in arr:
    numbers.append(int(n))
print("Max =", max(numbers))
print("Min =", min(numbers))

