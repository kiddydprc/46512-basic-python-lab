def tablemake():
    global n, limit
    
    i=1
    while(i<=limit):
        print(n, 'x', i, '= ', n*i)
        i+=1


n=int(input("n= "))
limit=int(input("limit= "))
tablemake()