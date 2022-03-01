def __main__():
    ages = [16, 18, 21, 18]
    print(ages)

    # The ".append()" add a element in last position
    ages.append(20)
    print("After add an element: ", ages)

    # The ".remove()" remove the first match element in the list
    ages.remove(18)
    print("After remove the element '18': ", ages)

    # The ".clear()" removes all the elements
    ages.clear()
    print("After clearing the elements: ", ages)


if __name__ == "__main__":
    __main__()
