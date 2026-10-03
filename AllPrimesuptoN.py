N = int(input("enter an integer"))

prime = [True] * (N + 1)
p = 2

prime[0]=False
prime[1]= False

while p*p <= N :
    if prime[p] == True:
        for i in range (p*p , N+1 , p):
            prime[i]=False
    p = p+1


for i in range (2 , N+1):
    if prime[i]==True:
        print(i)