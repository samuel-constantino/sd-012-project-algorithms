def verify_duplicate(sorted_nums):
    for i in range(len(sorted_nums)):
        if sorted_nums[i] < 0:
            return False
        if sorted_nums[i] == sorted_nums[i + 1]:
            return sorted_nums[i]


def find_duplicate(nums):
    # sorted_nums = merge_sort(nums)
    try:
        return verify_duplicate(sorted(nums))
    except IndexError:
        return False
    except TypeError:
        return False
