def main(s):
    s = s // 10
    n = 1

    while s < 51:
        s = s + 5
        n = n * 2

    return n


if __name__ == "__main__":
    for test in range(0, 1000):
        out = main(test)

        if out == 64:
            print(test) #210

            break #end
        
        else:
            continue

