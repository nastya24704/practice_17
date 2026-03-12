def determine_shape -> None:
    """
    Determines the shape of an object by its name.

    The function reads:
    - N - number of lines in the dictionary
    - N lines: first word is shape, rest are objects of this shape
    - Object name to find shape for

    Prints the shape of the object or the word itself if object is not found.
    """
    n = int(input("Enter the number of dictionary lines: "))
    shape_dict = {}

    print("Enter dictionary lines (shape objects): ")
    for _ in range(n):
        data = input().split()
        shape = data[0]
        for item in data[1:]:
            shape_dict[item] = shape

    target = input("Enter object name: ").strip()
    result = shape_dict.get(target, target)

    print(result)


if __name__ == "__main__":
    determine_shape()
