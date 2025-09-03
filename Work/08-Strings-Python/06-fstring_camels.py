years = float(input())
count = float(input())
animal = input()

#if it in intiger, delete .0
def fmt(x):
    if x.is_integer():
        return int(x)
    return x

print(f"In {fmt(years)} years I have spotted {fmt(count)} {animal}.") #f-string
