import cython


cpdef list mul(list matrix1, list matrix2):
    cdef int rows1 = len(matrix1)
    cdef int cols1 = len(matrix1[0])
    cdef int rows2 = len(matrix2)
    cdef int cols2 = len(matrix2[0])

    cdef int x, y
    if cols1 != rows2:
        print("Матрицы не могут быть умножены.")
        return None

    cdef list result = [[0 for x in range(cols2)] for y in range(rows1)]
    cdef int i, j, k

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += <int>(matrix1[i][k]) * <int>(matrix2[k][j])

    return result