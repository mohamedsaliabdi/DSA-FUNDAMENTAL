arr = [2, 3, 9]
total = 0
prime = []
for n in arr:
    is_prime = True
    if n < 2:
        is_prime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break

    if is_prime:
        prime.append(n)
        total += n

print("Prime numbers:", prime)
print("Sum of prime numbers:", total)