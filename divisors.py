M = int(input("enter a number"))
count = 0
answer = []
for i in range (1, M+1):

    if M % i == 0 :
        count +=1
        answer.append(i)
print(f"{count} {answer}")
    
        

