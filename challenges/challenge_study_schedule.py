def study_schedule(permanence_period, target_time):
    count = 0
    try:
        for student_period in permanence_period:
            if student_period[0] <= target_time <= student_period[1]:
                count += 1
    except TypeError:
        return None

    return count
