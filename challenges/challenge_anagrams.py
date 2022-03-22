def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2

    left, right = merge_sort(string[:mid]), merge_sort(string[mid:])

    return merge(left, right)


def merge(left, right):
    left_cursor, right_cursor = 0, 0
    merged = ''

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged += left[left_cursor]
            left_cursor += 1
        else:
            merged += right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged += left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged += right[right_cursor]

    return merged


def is_anagram(first_string, second_string):
    try:
        first_str = first_string.lower()
        second_str = second_string.lower()
        return merge_sort(first_str) == merge_sort(second_str)

    except IndexError:
        return False
