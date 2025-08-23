def isprime(n):
    prime=True
    i=2
    if(n>1):
        while(i!=n):
            if(n%i==0):
                prime=False
                break
            i+=1
    else: prime=False

    if(prime): print(n, "is prime")
    else: print(n, "is not prime")

n=int(input())
while(n!=0):
    isprime(n)
    n = int(input())