numbersTaken = [1, 2, 4, 12, 16]

print("Here is the free numbers:")
for n in range(1,20):
    if n in numbersTaken:
        continue
    print(n)
