a = 174457
b = 174505
k = 0

for n in range(a, b + 1):
    ds = []
    for d in range(2, n//2 + 1):
        if n % d == 0:
            ds.append(d)
            if len(ds) > 2:
                break

    if len(ds) == 2:
        print(ds[0], ds[1])