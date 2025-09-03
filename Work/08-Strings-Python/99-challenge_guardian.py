while True:
    line = input().strip()
    if line == "done":
        break
    if line.startswith("#"):
        continue
    print(line)
