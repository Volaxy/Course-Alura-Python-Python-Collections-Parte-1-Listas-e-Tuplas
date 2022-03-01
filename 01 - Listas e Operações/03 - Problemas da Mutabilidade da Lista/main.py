def __main__():
    ages = [16, 18, 21, 18]
    print(ages)

    print_list_length(ages)


def print_list_length(elements=None):
    if elements is None:
        elements = []

    print(len(elements))

    # The problem to manages the same list address, is the security problem, the recommended thing would be to mess with
    # a copy of the list, not its address, why the original list can be changed
    elements.append(15)


if __name__ == "__main__":
    __main__()
