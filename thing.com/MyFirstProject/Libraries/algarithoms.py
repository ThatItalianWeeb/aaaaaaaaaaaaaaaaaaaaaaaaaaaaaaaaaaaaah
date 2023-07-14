entries = [32, 14, 89, 62, 10, 20, 88, 40, 22, 91, 88, 65]


def linear_search(values, key):
    for i in range(len(values)):
        if values[i] == key:
            return i

    return -1


print(linear_search(entries, 88))


