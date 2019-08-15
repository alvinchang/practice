def matrix_spiral(matrix):
    """
    Returns the matrix in a spiral format in a list.

    [
     [ 1, 2, 3 ]
     [ 4, 5, 6 ]
     [ 7, 8, 9 ]
                ]

     => 1, 2, 3, 6, 9, 8, 7, 4, 5

    """

    r_end = len(matrix) - 1
    c_end = len(matrix[0]) - 1

    r_start = 0
    c_start = 0

    result = []

    while r_start <= r_end and c_start <= c_end:

        # Left-To-Right
        for _ in xrange(c_start, c_end + 1):
            result.append(matrix[r_start][_])

        # Increment row index
        r_start += 1

        # Top-To-Bottom
        for _ in xrange(r_start, r_end + 1):
            result.append(matrix[_][c_end])

        # Decrement column length
        c_end -= 1

        # Right-To-Left
        for _ in xrange(c_end, c_start - 1, -1):
            result.append(matrix[r_end][_])

        # Decrement row length
        r_end -= 1

        # Bottom-To-Top
        for _ in xrange(r_end, r_start - 1, -1):
            result.append(matrix[_][c_start])

        # Increment column index
        c_start += 1

    return result
