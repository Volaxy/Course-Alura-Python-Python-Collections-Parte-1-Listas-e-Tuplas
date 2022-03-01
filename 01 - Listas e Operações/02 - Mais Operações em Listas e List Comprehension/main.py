def __main__():
    ages = [16, 18, 21, 18]
    print(ages)

    # The "in" verify if the values is in the list, returning a boolean
    print(16 in ages)
    print(17 in ages)

    # The ".insert()" add an element in the specified position of the list
    ages.insert(2, 40)
    print("Insert a element in specified index: ", ages)

    # The ".extend()" add various elements at once in the list, the method receive an iterable
    ages.extend([8, 14])
    print("Add various elements at once: ", ages)

    # The "[OPERATION for ELEMENT in LIST]" builds a new list according to the operation, applied to each element at the
    # list
    print("Operation in the list: ", [age + 1 for age in ages])

    # The "if" filter each element of the list
    print("Filtering the elements of a list: ", [age for age in ages if age > 18])


if __name__ == "__main__":
    __main__()
