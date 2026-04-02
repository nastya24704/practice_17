def sort_words(s: str) -> str:
    """
    Returns words sorted by decreasing frequency of occurrence in the string.

    Args:
        s (str): Input string with words separated by spaces

    Returns:
        str: String with words sorted by decreasing frequency
    """
    words = s.split()
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    sorted_words = sorted(counter.keys(), key=lambda x: counter[x], reverse=True)
    return '\n'.join(sorted_words)


def main():
    input_str = input()
    result = sort_words(input_str)
    print(result)


if __name__ == "__main__":
    main()
