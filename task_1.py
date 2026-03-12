import collections

def sort_words(s: str) -> str:
    """
    Returns words sorted by decreasing frequency of occurrence in the string.

    Args:
        s (str): Input string with words separated by spaces

    Returns:
        str: String with words sorted by decreasing frequency
    """
    words = s.split()
    counter = collections.Counter(words)
    sorted_words = sorted(counter.keys(), key=lambda x: counter[x], reverse=True)
    return '\n'.join(sorted_words)


def main():
    input_str = input()
    result = sort_words(input_str)
    print(result)


if __name__ == "__main__":
    main()
