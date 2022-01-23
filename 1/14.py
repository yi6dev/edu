def main(x):
    q = 9
    l = 0

    while x >= q:
        l = l + 1
        x = x - q

    m = x

    if m < l:
        m = l
        l = x

    return l, m


if __name__ == "__main__":
    results = []
    for test in range(1, 1000):
        if main(test) == (4, 5):
            results.append(test)

    print(max(results)) #49
