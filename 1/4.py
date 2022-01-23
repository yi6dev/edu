size = 128 * 320 #px
weight = (20 * (2 ** 10) * (2 **3)) #bit


if __name__ == "__main__":
    for test in range(1, 10):
        if size*test == weight:
            print(test**2) #16

            break

        else:
            continue