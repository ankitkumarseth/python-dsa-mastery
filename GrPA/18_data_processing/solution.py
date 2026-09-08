from collections import Counter


def row_index_with_most_number_of_zeros(matrix: list) -> int:
    '''
    Given a matrix, find the index of the row with the 
    maximum number of zeros in it.

    Arguments: matrix: list[list] 
    Rertun: int - index of the row with the maximum number of zeros.
    '''
    max_zeros = 0
    index = 0
    for i, row in enumerate(matrix):
        if row.count(0) > max_zeros:
            max_zeros = row.count(0)
            index = i
    return index

    # return max(range(len(matrix)), key=lambda i: matrix[i].count(0))

def courses_sorted_by_enrollment(student_courses: dict) -> list:
    '''
    Given a dictionary of student roll numbers 
    with the list of courses they chose, 
    find the courses sorted from the 
    most number of enrollments to the least.

    Assume no courses will have the same number of students enrolled.

    Args:
    student_courses (dict): 
        a dictionary where keys are student roll numbers and 
        values are lists of courses they chose

    Returns:
    list: 
        a list of courses sorted by the number of students enrolled 
        in descending order
    '''
    all_courses = []
    for courses in student_courses.values():
        all_courses.extend(courses)
    course_counts = Counter(all_courses)
    return sorted(course_counts.keys(), key=course_counts.get, reverse=True)

def num_to_word(num: int) -> str:
    '''
    Given an integer, generate a string with its digits as words separated by hyphens.

    Arguments:
    num: int - the input number

    Return:
    str - the string with digits as words separated by hyphens
    '''
    dict_int_to_word = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
    }
    return '-'.join(dict_int_to_word.get(digit) for digit in str(num))

if __name__ == '__main__':
    # Problem 3: Antakshari property longest sub-sequence
    # Take the input from standard input using input()
    # and print the output according to the problem .
    
    # Write your code here for Problem 3
    word_count = int(input())
    for _ in range(word_count):
        words = input().split(',')
        current_length = 1
        max_length = 1 if words else 0
        for i in range(1, len(words)):
            if words[i-1][-1] == words[i][0]:
                current_length += 1
                if current_length > max_length:
                    max_length = current_length
            else:
                current_length = 1
        print(max_length)






