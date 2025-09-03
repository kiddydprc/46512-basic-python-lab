a = input().lower() #case insensitive
b = input().lower()

#dictionary order
if a < b:
    print("A comes before B")
elif a > b:
    print("A comes after B")
else:
    print("A equals B")
