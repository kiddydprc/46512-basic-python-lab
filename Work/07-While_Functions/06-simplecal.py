def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
while True:
    choice = int(input())
    if choice == 4:
        print("Ended of the program")
        break
    a = int(input())
    b = int(input())
    if choice == 1:
        print("Result:", add(a, b))
    elif choice == 2:
        print("Result:", sub(a, b))
    elif choice == 3:
        print("Result:", mul(a, b))
