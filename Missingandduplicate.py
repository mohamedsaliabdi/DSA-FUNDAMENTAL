arr = [1, 2, 3, 3, 5, 6]

N = len(arr)

expected_sum = N * (N + 1) // 2
actual_sum = sum(arr)

expected_square_sum = N * (N + 1) * (2 * N + 1) // 6

actual_square_sum = 0

for n in arr:
    actual_square_sum += n * n

difference = expected_sum - actual_sum

square_difference = expected_square_sum - actual_square_sum

sum_missing_duplicate = square_difference // difference

missing = (difference + sum_missing_duplicate) // 2

duplicate = sum_missing_duplicate - missing

print("Missing =", missing)
print("Duplicate =", duplicate)