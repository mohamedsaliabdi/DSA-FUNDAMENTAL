def power(b, e):
    result = 1
    for i in range(e):
        result = result * b
    return result

print(power(5,2))