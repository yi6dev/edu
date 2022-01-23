import random

letters = list("ШОЛА") # [..., ...]


if __name__ == "__main__":
    iterations = 10000

    index = 0
    words = []

    while 1:
        l = []

        l.append(random.choice(letters))
        l.append(random.choice(letters))
        l.append(random.choice(letters))

        k_pos = random.randint(0, 2)

        l[k_pos] = "К"

        word = l[0]+l[1]+l[2]

        if word not in words:
            words.append(word)

        index += 1

        if iterations < index:
            break

    print(len(words))
    print(words)