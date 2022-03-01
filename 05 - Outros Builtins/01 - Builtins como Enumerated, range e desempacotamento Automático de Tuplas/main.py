def __main__():
    ages = [19, 20, 21, 18, 24]

    # for i in range(len(ages)):
    #    print(i, ages[i])

    print(enumerate(ages))
    print(list(enumerate(ages)))

    # This is known as unpacking
    for index, value in enumerate(ages):
        print(index, value)

    users = [
        ("Guilherme", 15, 1987),
        ("Gustavo", 21, 2000),
        ("Fabian", 20, 1998)
    ]

    # The "_" indicates which the 2º and 3º argument of each value will not be used
    for name, _, _ in users:
        print(name)


if __name__ == "__main__":
    __main__()
