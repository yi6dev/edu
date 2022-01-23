numbers = []

for index in range(1016, 7937):
    if not index % 3:
        if index % 7:
            if index % 17:
                if index % 19:
                    if index % 27:
                        numbers.append(index)

print(f"Count: {len(numbers)}")
print(f"Max: {max(numbers)}")