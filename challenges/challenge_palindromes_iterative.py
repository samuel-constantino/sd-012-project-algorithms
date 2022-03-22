def reverse(word):
    word_reverse = []
    for c in word:
        word_reverse.insert(0, c)
    return "".join(word_reverse)


def is_palindrome_iterative(word):
    if word == '':
        return False

    # word_reverse = reverse(word)

    return word == word[::-1]
