N = int(input("enter the number of integer"))

arr = list(map(int, input("enter the integers separated by space: ").split()))

answer = arr[0]
for i in range (1 , N):
    a = answer
    b= arr[i]

    while b!=0:
        reminder = a%b
        a = b
        b = reminder
    gcd = a

    answer = (answer//gcd)*arr[i]

print("LCM of the array is:", answer)