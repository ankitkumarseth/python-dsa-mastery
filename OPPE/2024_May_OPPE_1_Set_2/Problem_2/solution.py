def row_index_with_most_number_of_zeros(matrix:list)->int:
    '''
    Given a matrix, find the index of the row with the
    maximum number of zeros in it.

    Arguments: matrix: list[list]
    Rertun: int - index of the row with the maximum number of zeros.
    '''

    return max(range(len(matrix)), key=lambda i: matrix[i].count(0))
    # Basic way of solving
    # zero_count = -1
    # index = None
    # for i, row in enumerate(matrix):
    #     current_zeros = row.count(0)
    #     if current_zeros > zero_count:
    #         zero_count = current_zeros
    #         index = i
    # return index



