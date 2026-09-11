arr = [10, 20, 30, 40, 50]

largest = arr[0]
second_largest = arr[1]
smallest = arr[0]
second_smallest = arr[1]
for n in arr:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n

    if n < smallest :
        second_smallest = smallest
        smallest = n
    elif n < second_smallest and n != smallest:
        second_smallest = n 
print(largest)
print(second_largest)
print(smallest)
print(second_smallest)