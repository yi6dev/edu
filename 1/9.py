x = 49**7 + 7**21 - 7

count = 0
while x > 0:
    if x % 7 ==6:
        count += 1

    x = x // 7

print(count) #13 