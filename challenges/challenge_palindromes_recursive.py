def reverse(word):
    if len(word) < 2:
        return word

    return reverse(word[1:]) + word[0]


def is_palindrome_recursive(word, _low_index, _high_index):
    if word == '':
        return False

    word_reverse = reverse(word)

    if word == word_reverse:
        return True

    return False
