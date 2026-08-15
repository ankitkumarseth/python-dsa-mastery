import collections


def courses_sorted_by_enrollment(student_courses: dict) -> list:
    '''
    Given a dictionary of student roll numbers
    with the list of courses they chose,
    find the courses sorted from the
    most number of enrollments to the least.

    Assume no courses will have the same number of students enrolled.

    Arguments:
    student_courses: dict - a dictionary where keys are
        student roll numbers and values are lists of courses they chose

    Return:
    list - a list of courses sorted by the
        number of students enrolled in descending order
    '''
    courses = [course for courses in student_courses.values() for course in courses]
    count = collections.Counter(courses)
    return [course for course, freq in count.most_common()]

    # Alternate Solution Without Counter
    # counts = collections.defaultdict(int)
    # for courses in student_courses.values():
    #     for course in courses:
    #         counts[course] += 1
    #
    # 2. Sort the keys of the dict based on their values
    # return sorted(counts, key=counts.get, reverse=True)
