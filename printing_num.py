start = 1
for i in range(1, 5):
    for j in range(start, start + i):
        print(j, end=' ')
    print()
    start += i